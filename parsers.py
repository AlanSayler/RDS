import logging
import config
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#don't use this, will fix later
def parseForEmail(xml, quests):
   resp = quests
   y = BeautifulSoup(xml,"lxml")
   for i in range (0,len(len(quests))):
      quests[i] = 'q' + quests[i]
      resp[i] = (y.find(quests[i]).string)
   return resp

#pass questreferences
def parseForEmails(xml, quests):
   print(xml)
   y = BeautifulSoup(xml,"lxml")
   addresses = y.findAll('emailaddress')
   xran = len(addresses)
   yran = (len(quests) + 1)
   d = [['' for x in range(yran)] for x in range(xran)]
   for i in range (0,xran):
      d[i][0] = addresses[i].string
      for j in range(1,yran):
         d[i][j] = y.findAll(quests[j-1])[i].string
         #attach suffix if it isn't there
         if d[i][j] != None:
            if d[i][j].find('@') == -1:
               d[i][j] = d[i][j] + config.suffix
   return d       
