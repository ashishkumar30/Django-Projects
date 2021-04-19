#{"Luka Chuppi":"2019-03-01","Badla":"2019-03-08","Kesari":"2019-03-21","Gully Boy":"2019-02-14","Total Dhamaal":"2019-02-22"}

# import function database_scraping_controller from base.py file
from base import database_scraping_controller

""" Configure Database Credentials **Change here"""

# database Credentials change credentials according to database

hostname = "localhost"
username = "ashish2"
password = "ashish@123"
database = "db"
# Tabe name by default is Movie_table

"""  Input in dictionary format as per sample :- {"Luka Chuppi":"2019-03-01","Badla":"2019-03-08"}  """

# inputs as per sample
input_dictionary = {"Luka Chuppi": "2019-03-01", "Badla": "2019-03-08", "Kesari": "2019-03-21",
                    "Gully Boy": "2019-02-14", "Total Dhamaal": "2019-02-22"}

""" Run Function """


def main(input_dictionary):
    # extract every element of dictionary ,Scrap data and save to database
    for details in input_dictionary.items():
        name, date = details
        print("Movie Name is", name, "Releasing date is", date)
        try:
            database_scraping_controller(hostname, username, password, database, name=name, date=date)
            print("Complete data of movie", name)
        except Exception as e:
            print("Error in Input of movie", name,str(e))


# run func
main(input_dictionary)
