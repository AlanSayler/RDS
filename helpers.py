import random
import config
import filemanager
def chooseSurvey():
   coin = random.randint(1,2)
   if coin == 1:
      return config.survey1id
   return config.survey2id

#returns index of specified email
def findEmail(users,id):
   for i in range(0, len(users)):
      if id == users[i].email:
         index = i
   return index

def getParentList(users,index):
   arr = [users[index].email]
   done = 0
   if not users[index].parentID:
      return arr 
   while not done:
      index = findEmail(users,users[index].parentID)
      arr.append(users[index].email)
      if not users[index].parentID:
         done = 1
   return arr

def calcDist(lista,listb):
   dist = 0
   if not lista or not listb:
      return dist
   if all(x is None for x in lista) or all(x is None for x in listb):
      return dist
   for i in range(0,len(lista)):
      for j in range(0,len(listb)):
         if lista[i] == listb[j]:
            dist = i + j
   return dist 
