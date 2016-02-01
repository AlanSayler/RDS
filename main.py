
import urllib
import config
import quapi
import parsers
import helpers
import filemanager
from datetime import datetime, timedelta
#load config.
config.init()

#read old csv to get data.
arr =  filemanager.readcsv(config.filename)
users = filemanager.arrayToUsers(arr)
precount = 0
for i in range(0,len(users)):
   if users[i].state == 'c':
      precount = precount +1


#query qualtrics for responses
xmlresp1 = quapi.makeRequest(quapi.getLegacyResponseData(config.survey1id, config.survey1questions))
xmlresp2 = quapi.makeRequest(quapi.getLegacyResponseData(config.survey2id,config.survey2questions))

arr1 = parsers.parseForEmails(xmlresp1,config.survey1refs)
arr2 = parsers.parseForEmails(xmlresp2,config.survey2refs)

#integratge new responses with old data, set repeats and invalids to D, set completed surveys to C, send them thank yous
for i in range(0,len(arr1)):
   for j in range(0,len(users)):
      if arr1[i][0] == users[j].email:
         users[j].state = 'c'
         for k in range(0,len(users[j].childrenID)):
            users[j].childrenID[k] = arr1[i][k+1]
            users[j].childrenID[k] = users[j].childrenID[k].replace(' ', '')
#I know this is dumb, but it's late at night, and I'm confusing passing users by value or reference in my head, so this is what I'm doing.
for l in range(0,len(arr2)):
   for m in range(0,len(users)):
      if arr2[l][0] == users[m].email:
         users[m].state = 'c'
         for n in range(0,len(users[m].childrenID)):
            users[m].childrenID[n] = arr2[l][n+1]
            users[m].childrenID[n] = users[m].childrenID[n].replace(' ', '')

postcount = 0
for i in range(len(users)):
   if users[i].state == 'c':
      postcount = postcount + 1

credits = (postcount - precount) * 3
#kill all nonvalid surveys
if config.allowOnlySuffixes == 1:
   for i in range(0,len(users)):
      if config.suffix not in users[i].email:
         users[i].state == 'd'

#kill expired surveys
for i in range(len(users)):
   if (users[i].sendTime + config.expiry) < datetime.now() and users[i].state == 's':
      users[i].state = 'd'
      credits = credits + 1

for i in range(0, len(users)):
   if users[i].state == 'c':
      for j in range(0, len(users[i].childrenID)):
         found = 0
         for k in range(0, len(users)):
            if users[i].childrenID[j] == users[k].email:
               found = 1
         if found == 0:
            if not not users[i].childrenID[j]:
               new = filemanager.User()
               new.email = users[i].childrenID[j]
               new.email = new.email.replace(' ', '')
               new.parentID = users[i].email
               new.state = 'n'
               users.append(new)


#check for Qs more than 1 day old, send surveys, set state to S
for i in range(0,len(users)):
   if users[i].state == 'q' and datetime.now() > (users[i].selectTime + config.delay):
      surv = helpers.chooseSurvey()
      subj = ''
      if users[i].parentID == '':
         subj = config.subject
      else:
         subj = config.subject2 + users[i].parentID
      quapi.sendSurveySubjectExpiry(users[i].email, surv,subj) 
      users[i].state = 's'
      users[i].timeSent = datetime.now()   
      users[i].survey = surv
#calculate ave distance of each N to Qs and Ss and Cs
listofListOfParents = [None] *len(users)
dists = [0] * len(users)
for i in range(0,len(users)):
   listofListOfParents[i] = helpers.getParentList(users,i)
for i in range(0,len(users)):  
   if users[i].state == 'n':
      if not users[i].parentID:
         dists[i] = 10000
      else:
          
         for j in range(0,len(users)):
            if users[j].state == 's'or users[j].state == 'c' or users[j].state == 'q':
               dists[i] = dists[i] + helpers.calcDist(listofListOfParents[i],listofListOfParents[j])

running = 0
for i in range(0,len(users)):
   if users[i].state == 's' or users[i].state == 'c' or users[i].state == 'q':
      running = running +1
#set Ns to Qs until either credits, total coupons are exceeded.
while credits > 0 and running < config.total:
   index = dists.index(max(dists))
   if users[index].state == 'n':
      users[index].state = 'q'
      users[index].selectTime = datetime.now()
      credits = credits-1
      running = running + 1
   dists[index] = 0
   found = 0
   for i in range(0,len(users)):
      if users[i].state == 'n':
         found = 1
   if not found:
      credits = 0
#write to csv
filemanager.writecsv(filemanager.usersToArray(users), config.filename)

