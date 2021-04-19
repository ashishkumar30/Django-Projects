# import all libraries

try:
    import mysql.connector as connector
    from bs4 import BeautifulSoup
    import re
    import requests
    import pandas as pd
    from pandas.tseries.offsets import Day
    from datetime import datetime

except Exception as e:
    print("Exception in Import", str(e))


class Database:
    """ Class to work with database , Store data in database"""

    def __init__(self, host, username, password, database):

        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection_object = connector.connect(host=self.host,
                                                   username=self.username,
                                                   password=self.password,
                                                   database=self.database,
                                                   )

    def create_table(self, ):

        try:
            cur = self.connection_object.cursor()

            # create table if NOT exist

            cur.execute(
                "create table if not exists Movie_table(MovieName varchar(200) not null, DaysfromRelease varchar(20) not null, Date varchar(30) not null, BoxOfficeCollection varchar(20) not null)")

        except Exception as e:

            print("Error in creating table", str(e))
            self.connection_object.rollback()

    def insert_data(self, movie_name_insert, day_insert, converted_day_insert, collection_insert):

        # insert data to table

        cur = self.connection_object.cursor()
        try:
            sql = "insert into Movie_table(MovieName, DaysfromRelease, Date, BoxOfficeCollection) values (%s, %s, %s, %s)"

            # The row values are provided in the form of tuple
            val = (movie_name_insert, day_insert, converted_day_insert, collection_insert)

            # inserting the values into the table
            cur.execute(sql, val)

            # commit the transaction
            self.connection_object.commit()
            # print("Record Inserted")

        except Exception as e:

            print("Error in inserting record", str(e))
            self.connection_object.rollback()

    def show_table_data(self):

        try:
            cur = self.connection_object.cursor()
            cur.execute("select * from Movie_table")
            # fetching the rows from the cursor object
            result = cur.fetchall()
            # printing the result

            print("Fetching all data from table")

            for data_fetch in result:
                print(data_fetch)

        except Exception as e:
            print("Error while fetching data", str(e))
            self.connection_object.rollback()

        # close all now
        self.connection_object.close()


class DataExtractor:
    """ Class to work with Data Extraction- Scraping from website and cleaning data """

    def __init__(self, movie_name, releasing_date_):

        self.movie_name = movie_name
        self.releasing_date_ = releasing_date_

    def converting_cr(self, amount):

        """
        To Change CR to integer value
        float variable after taking out the currency and other signs. So 17.90 Cr will be stored as 179000000
        """
        return int(float(amount.split()[0][1:]) * 10000000)

    def date_change(self, days, releasing_date_new):

        """
        TO change date format  If the movie release date is 2019-03-01 and Days from release is 2,
        then the date should be stored as 2019-03-02 (MM is 03, DD is 02 and YYYY is 2019 as it is the second day)
        """

        input_date = datetime(int(releasing_date_new[0]), int(releasing_date_new[1]), int(releasing_date_new[2]))
        output_date = input_date + int(days) * Day()

        # return date with new format
        return output_date.strftime('%d/%m/%Y')

    def getting_date_change_format(self, one_entry):

        """
        if Identify if two dates are in single entry ex: Day 24 - to day 26
        """

        releasing_date_new = self.releasing_date_.split("-")
        if "-" in one_entry:
            starting_days = one_entry.split("-")[0].split()[-1]
            starting_day = self.date_change(starting_days, releasing_date_new)
            ending_days = one_entry.split("-")[1].split()[-1]
            ending_day = self.date_change(ending_days, releasing_date_new)
            full_date = starting_day + " " + ending_day
        else:
            days = one_entry.split()[-1]
            full_date = self.date_change(days, releasing_date_new)

        cleaning_date = full_date.replace("/", "-")

        # return clean date
        return cleaning_date.replace(" ", " - ")

    def return_dictionary_for_dataframe(self, table_data):

        """
        It return all data in form of Dictionary wth keys Name, Days, Changed_Dates, Amount
        """

        # to make dictionary
        all_days, changed_dates, converted_amount_all, movie_name_all = [], [], [], []

        for days_amount in table_data:
            day_, amount_ = days_amount

            # adding days and amount for dataframe
            all_days.append(day_)

            # converting date in new format
            changed_date_output = self.getting_date_change_format(day_)
            changed_dates.append(changed_date_output)

            # converting amount
            amount_converted = self.converting_cr(amount_)
            converted_amount_all.append(amount_converted)

            # movie name if iteration required
            movie_name_all.append(self.movie_name.replace("-", ' '))

        # return a dictionary consist of all clean and converted data
        return {"Name": movie_name_all,
                "Days": all_days,
                "Changed_Dates": changed_dates,
                "Amount": converted_amount_all
                }

    def scrap_data(self, ):

        """
        Scrap the HTML given page and extract all data and clean data to get results,
        """

        # full url
        full_url = ''.join(f"​https://boxofficecollection.in/{self.movie_name}-box-office-collection-day-wise".split()).replace('\u200b', '')

        # extracting data from SOUP and GET information of Required table
        req = requests.get(full_url)
        soup = BeautifulSoup(req.content, 'html5lib')
        for x in soup.findAll("div", {"class": re.compile(r"\btd-pb-span8 td-main-content\b")}):
            soup_object = str(x).split("Box Office Verdict")[1].split("Total")[0]
        days_clean, collection_clean = [], []
        for x in soup_object.split(">"):
            if "Day" in x:
                days_clean.append(x.split("<")[0])
            elif "₹" in x:
                collection_clean.append(x.split("<")[0])

        # zip to make table data
        table_data = list(zip(days_clean, collection_clean))

        # return dictionary
        dict_response = self.return_dictionary_for_dataframe(table_data)

        return dict_response


def database_scraping_controller(*args, **kwargs):
    """
    This is main function which control all the flow of programme
    getting all inputs from user/file ** are Database inputs and ** are the date and name of movie
    """

    string_correct = kwargs.get("name")
    date_correct = kwargs.get("date")

    # cleaning string and correcting it according to input
    string_correct = '-'.join(string_correct.replace("-", ' ').strip().split())

    # making object of database
    database_obj = Database(*args)
    # creating table if not created
    database_obj.create_table()

    # Extracting all information of data
    object_ = DataExtractor(string_correct, date_correct)
    extracted_data = object_.scrap_data()

    # converting to dataframe
    df = pd.DataFrame(extracted_data)
    # print("DataFrame,df)

    # creating a txt for trial

    movie_name_insert = "Movie Name"
    day_insert = "Days from Release"
    converted_day_insert = "Days"
    collection_insert = "Box Office Collection"

    output = f"{movie_name_insert}       {day_insert}       {converted_day_insert}       {collection_insert}" + " \n"
    with open("Movie_table_output.txt", 'a+') as testfile:
        testfile.write(output)

    # inserting to database one by one
    for entry in range(len(df)):
        try:
            single_entry = df.iloc[entry].to_list()
            movie_name_insert = str(single_entry[0])
            day_insert = str(single_entry[1])
            converted_day_insert = str(single_entry[2])
            collection_insert = str(single_entry[3])

            # inserting data to MYSQL database
            database_obj.insert_data(movie_name_insert, day_insert, converted_day_insert, collection_insert)

            # saving single entry to file also
            with open("Movie_table_output.txt", 'a+') as testfile:
                details = f"{movie_name_insert:20} {day_insert:20}  {converted_day_insert:30}  {collection_insert:20}" + " \n"
                testfile.write(details)

        except Exception as e:
            print("error in inserting data of single entry", str(e))

    # after completing every movie detail fetch information from database
    database_obj.show_table_data()
