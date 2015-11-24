import config
import urllib.request
import logging
def makeRequest (url):
    return urllib.request.urlopen(url).read()


def addRecipient (emailaddress):
    url = config.basicurl + 'addRecipient' + config.midurl + '&LibraryID=' + config.library + '&PanelID=' + config.panel + '&Email=' + emailaddress + config.suffix
    return url

def sendSurveyToIndividual (recipient, survey):
    url = config.basicurl + 'sendSurveyToIndividual' + config.midurl + '&SurveyID=' + survey + '&SendDate=2015-01-01%2000%3A00%3A00&FromEmail=' + config.fromwho + '&FromName=' + config.fromname + '&Subject=' + config.subject + '&MessageID=' + config.message + '&MessageLibraryID=' + config.library + '&PanelID=' + config.panel + '&PanelLibraryID=' + config.library + '&RecipientID=' + recipient
    return url
