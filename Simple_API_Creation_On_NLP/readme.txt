# Creating API on Django using Natural Language Processing -Spacy in backend.
# This Simple API on Django takes string as an input and give response of Part of speech of every word in string using SPACY.
# It will takes both Get and Post requests.
#First start virtual environment startproject using command 

cd start_project
cd scripts
activate.bat
cd..
cd..
python manage.py runserver

#OR --

#install all requirments using command 

pip install -r requirments.txt

python -m spacy download en_core_web_sm

python manage.py runserver

# pass data in json format {"data":"This is Ashish"}
# API will now give response with part of speach of every word.
