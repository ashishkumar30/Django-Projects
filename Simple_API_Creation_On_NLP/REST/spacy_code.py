
from logging import *
logformat='{lineno} {name} {asctime} {message}'
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',style='{',format=logformat)

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    critical("Error in Loading en_core_web_sm")
    pass

variable=[]
def spacy_fun(data):
    try:
        info("Code is running Data inserted")
        doc=nlp(data)
        warning("Data is converted trough nlp")
        try:
            for token in doc:
                disp=(token.text, token.pos_, token.dep_)
                variable.append(disp)
                debug("Code run and output stored in Variable")
            return variable
        except:
            error("Error in Breaking data to chunks")
            return "Error in Chunk"
    except:
        critical("Error in data passing")
        return "Error in Data passing"


#spacy_fun(doc)