# df_assigment
Please find the assignment details in this [document](https://docs.google.com/document/d/1EGvCKhHCfo0GS4bwjuyX0Pk4uq2_-Vx88nqAmHl8b_g/edit?usp=sharing).


-------------
#### Project description

* Task to scrap data from given url + movies and save data to database.
* Data is stored in table name :- Movie_table
* Task is completed & output screenshots of mysql are attached, also a txt file is generated for reference.
* Main file to start application is config.py and base.py file have two Classes one for data extraction and other for Update data in Database.


```sh
config.py is main file to start application.
```

Change Database Mysql Configuration in config.py file from line 10 to 13 (** DB config)

```sh

hostname = "localhost"
username = "ashish2"
password = "ashish@123"
database = "db"

```
Input parameters :- line No 19 
```sh

change Inputdictionary variable with the new inputs .

input_dictionary

# inputs as per sample
input_dictionary = {"Luka Chuppi": "2019-03-01", "Badla": "2019-03-08", "Kesari": "2019-03-21",
                    "Gully Boy": "2019-02-14", "Total Dhamaal": "2019-02-22"}

```

Install all required libraries using

```sh

> - pip3 install -r "requirements.txt
> - run file - config.py is main file to start application. using:- python3 config.py 

```

Run Project

* config.py is main file to start application.

```sh

> - python3 config.py 

```

