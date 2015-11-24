from urllib2 import Request, urlopen, URLError

f = open("config.txt","r")
configs =[]
version = "2.5"
#do this different and better. For now, it takes some stuff from a file.
for line in f:
    configs.append(line)


rooturl = 'https://survey.qualtrics.com/WRAPI/ControlPanel/api.php'
token = configs[0].rstrip()
username = configs[1].rstrip()
username = username.replace('#', '%23')
library = configs[2].rstrip()
panel = configs[3].rstrip()
message = configs[4].rstrip()
suffix = configs[5].rstrip()
fromwho = configs[6].rstrip()
fromwho = fromwho.replace('@', '%40')
survey = configs[7].rstrip()
subject = 'You%27ve%20been%20invited%20to%20take%20a%20survey'
version = '2.5'
form = 'XML'
basicurl = rooturl + '?API_SELECT=ControlPanel&Version=' + version + '&Request='
midurl = '&User=' + username + '&Token=' + token + '&Format=' + form

def xmlfromurl (url):
    request = Request(url)
    try:
        response = urlopen(request)
        xml = response.read()
        return xml
    except URLError, e:
        print 'Could not make request', e

def addRecipient (emailaddress):
    url = basicurl + 'addRecipient'+midurl + '&LibraryID=' + library + '&PanelID=' + panel + '&Email=' + emailaddress + suffix
    return url


#work on this later to get times, possible customized messages
def sendSurveyToIndividual (recipient):
    url = basicurl + 'sendSurveyToIndividual' + midurl + '&SurveyID=' + survey + '&SendDate=2000-01-01%2000%3A00%3A00&FromEmail=' + fromwho + '&FromName=' + fromwho + '&Subject=' + subject  + '&MessageID=' + message + '&MessageLibraryID=' + library + '&PanelID=' + panel  + '&PanelLibraryID=' + library + '&RecipientID=' + recipient + '&SentFromAddress=' + fromwho
    return url

#work on this later to get questions and start/end date
def getLegacyResponseData ():

    return url

def sendThankYou ():

    return url

print(xmlfromurl(addRecipient('karlrohe')))
print(sendSurveyToIndividual('MLRP_eQj6YcvudJSsat7'))
