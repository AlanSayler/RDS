import config
import urllib.request
import logging
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
def makeRequest (url):
    response = urllib.request.urlopen(url)
    lines = bytes.decode(response.read())
    return lines

#I'm certain there's a better way of building urls than this, 
#but I'm not very smart, and am in a bit of a hurry
def addRecipient (emailaddress):
    e = emailaddress.replace('@', '%40')
    url = config.basicurl + 'addRecipient' + config.midurl + '&LibraryID=' + config.library + '&PanelID=' + config.panel + '&Email=' + e
    return url

def sendSurveyToIndividual (recipient, survey):
    url = config.basicurl + 'sendSurveyToIndividual' + config.midurl + '&SurveyID=' + survey + '&SendDate=2015-01-01%2000%3A00%3A00&FromEmail=' + config.fromwho + '&FromName=' + config.fromname + '&Subject=' + config.subject + '&MessageID=' + config.message + '&MessageLibraryID=' + config.library + '&PanelID=' + config.panel + '&PanelLibraryID=' + config.library + '&RecipientID=' + recipient + '&ExpirationDate=2017-01-01%2000%3A00%3A00'
    return url

def sendSurveyToIndividualSubjectExpiry (recipient, survey, subject):
    expirydatetime = datetime.now() + config.expiry
    expirystring = expirydatetime.strftime('%Y-%m-%d %H:%M:%S')
    expirystring = expirystring.replace(' ', '%20' )
    expirystring = expirystring.replace(':', '%3A')
    url = config.basicurl + 'sendSurveyToIndividual' + config.midurl + '&SurveyID=' + survey + '&SendDate=2015-01-01%2000%3A00%3A00&FromEmail=' + config.fromwho + '&FromName=' + config.fromname + '&Subject=' + subject + '&MessageID=' + config.message + '&MessageLibraryID=' + config.library + '&PanelID=' + config.panel + '&PanelLibraryID=' + config.library + '&RecipientID=' + recipient + '&ExpirationDate=' + expirystring
    print(expirystring)
    return url 
#change this to allow for different numbers of responses
def getLegacyResponseDataOfIndividual (recipientID, surveyID, quests):
    url = config.basicurl + 'getLegacyResponseData' + config.midurl + '&SurveyID=' + surveyID + '&ResponseID=' + recipientID   + '&Questions=QID' + quests[0] + '%2CQID' + quests[1] + '%2CQID' + quests[2] + '%2CQID' + quests[3] + '%2CQID' + quests[4]
    return url

def getLegacyResponseData (surveyID, quests):
    q = quests[0]
    for i in range(1,len(quests)):
        q = q + '%2CQID' + quests[i]
    url = config.basicurl + 'getLegacyResponseData' + config.midurl + '&SurveyID=' + surveyID + '&Questions=QID' + q 
    return url

def sendSurvey (emailaddress, survey):
    xml  = makeRequest(addRecipient(emailaddress))
    y  = BeautifulSoup(xml, "lxml")
    #print(y)
    thestring = str(y.html.body.xml.result.recipientid.string)
    #print(thestring)
    print(sendSurveyToIndividual(thestring,survey))
    response =  makeRequest(sendSurveyToIndividual(thestring, survey))
    return response

def sendSurveySubjectExpiry (emailaddress, survey, subject):
    xml  = makeRequest(addRecipient(emailaddress))
    y  = BeautifulSoup(xml, "lxml")
    #print(y)
    thestring = str(y.html.body.xml.result.recipientid.string)
    #print(thestring)
    response =  makeRequest(sendSurveyToIndividualSubjectExpiry(thestring, survey,subject))
    return response



