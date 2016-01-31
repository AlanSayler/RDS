import csv
from datetime import datetime, timedelta

class User:
   def __init__(self):
      self.email = ''
      self.state = 'n'
      self.parentID = ''
      self.childrenID = ['','','','','']
      self.survey = ''
      self.selectTime = datetime.now() - timedelta(days=100)
      self.sendTime = datetime.now() - timedelta(days = 100)
      self.returnTime = datetime.now() - timedelta(days = 100)


def writecsv(users,filename):
   with open(filename, 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter = ',')
      writer.writerows(users)
      
def readcsv(filename):
   file = open(filename, 'r')
   datareader = csv.reader(file,delimiter=',')
   d = []
   for row in datareader:
      d.append(row)
   return d 

def usersToArray(users):
   xran = len(users)
   yran = 12
   d = [['' for x in range(yran)] for x in range(xran)]
   for i in range (0,xran):
      d[i][0] = users[i].email
      d[i][1] = users[i].state
      d[i][2] = users[i].parentID
      for j in range(3, 3 + len(users[i].childrenID)):
         d[i][j] = users[i].childrenID[j-3]
      d[i][8] = users[i].survey
      d[i][9] = users[i].selectTime.strftime('%Y-%m-%d %H:%M:%S')
      d[i][10] = users[i].sendTime.strftime('%Y-%m-%d %H:%M:%S')
      d[i][11] = users[i].returnTime.strftime('%Y-%m-%d %H:%M:%S')
   return d

def arrayToUsers(arr):
   xran = len(arr)
   users = []
   for i in range(0,len(arr)):
      user = User()
      user.email = arr[i][0]
      user.state = arr[i][1]
      user.parentID = arr[i][2]
      for j in range(3,len(user.childrenID)):
         user.childrenID[j-3] = arr[i][j]
      user.survey = arr[i][8]
      user.selectTime = datetime.strptime(arr[i][9], '%Y-%m-%d %H:%M:%S')
      user.sendTime = datetime.strptime(arr[i][10], '%Y-%m-%d %H:%M:%S')
      user.returnTime = datetime.strptime(arr[i][11], '%Y-%m-%d %H:%M:%S')
      users.append(user)
   return users
   
