import config
import urllib.request
import logging
from bs4 import BeautifulSoup
def makeRequest (url):
    response = urllib.request.urlopen(url)
    lines = bytes.decode(response.read())
    return lines


def addRecipient (emailaddress):
    url = config.basicurl + 'addRecipient' + config.midurl + '&LibraryID=' + config.library + '&PanelID=' + config.panel + '&Email=' + emailaddress + config.suffix
    return url

def sendSurveyToIndividual (recipient, survey):
    url = config.basicurl + 'sendSurveyToIndividual' + config.midurl + '&SurveyID=' + survey + '&SendDate=2015-01-01%2000%3A00%3A00&FromEmail=' + config.fromwho + '&FromName=' + config.fromname + '&Subject=' + config.subject + '&MessageID=' + config.message + '&MessageLibraryID=' + config.library + '&PanelID=' + config.panel + '&PanelLibraryID=' + config.library + '&RecipientID=' + recipient + '&ExpirationDate=2017-01-01%2000%3A00%3A00'
    return url

def sendSurvey (emailaddress, survey):
    xml  = makeRequest(addRecipient(emailaddress))
    y  = BeautifulSoup(xml)
    thestring = str(y.html.body.xml.result.recipientid)
    thestring = thestring.strip('</recipientid>')
    thestring = thestring.strip('<recipientid>')
    response =  makeRequest(sendSurveyToIndividual(thestring, survey))
    return response




