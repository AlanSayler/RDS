import urllib
import config
import quapi
import parsers
import helpers
import filemanager
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

config.init()
survey = helpers.chooseSurvey()
quapi.sendSurvey(config.seedemail, survey)
users = []
x = filemanager.User()
x.state = 's'
x.sendTime = datetime.now()
x.selectTime = datetime.now()
x.email = config.seedemail
x.survey = survey

users.append(x)

filemanager.writecsv(filemanager.usersToArray(users),config.filename)
