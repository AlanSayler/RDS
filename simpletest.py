import urllib
import config
import quapi
import parsers
import filemanager
import numpy as np
import pandas as pd
config.init()

#print(quapi.makeRequest(quapi.addRecipient(config.seedemail)))
#print(quapi.makeRequest(quapi.sendSurveyToIndividual( 'MLRP_9YO0nUPyUo5vyDj', config.survey2id)))
#print((quapi.sendSurvey(config.seedemail,config.survey2id)))
filemanager.writecsv(parsers.parseForEmails(quapi.makeRequest(quapi.getLegacyResponseData(config.survey2id, config.survey2questions)),config.survey2refs), 'somefile.csv')

d = filemanager.readcsv('somefile.csv')
print(d[0][0])
filemanager.writecsv(d,'somefile.csv')

#print('\n\n\n')

#print(quapi.makeRequest(quapi.getLegacyResponseData(config.survey2id,config.survey2questions)))

#print(config.survey2questions[2])


#parsers.parseForEmail((quapi.makeRequest(quapi.getLegacyResponseDataOfIndividual('R_1gcgt9z0Oxa1B01', config.survey2id, config.survey2questions))), config.survey2questions)
