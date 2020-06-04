# This Simple API on Django takes string as an input and give response of Part of speech of every word in string using SPACY.
# It will takes both Get and Post requests.
#First start virtual environment startproject using command

cd startproject
cd scripts
activate.bat
cd..
cd..

# ** You can install en_web_core_sm  using command line

python -m spacy download en_core_web_sm

# start project using command

python manage.py runserver

# pass data in json format {"data":"This is Ashish and i am software developer"}
# API will now give response with part of speach of every word.
