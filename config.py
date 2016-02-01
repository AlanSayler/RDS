from datetime import datetime, timedelta
def init():

    #end users: edit the variables below this line, but above the line where
    #I tell you to stop
    global total
    total = 100
    global delay
    delay = timedelta(seconds = 1)
    global expiry 
    expiry = timedelta(days = 7)
    global filename
    filename = 'test.csv'
    global seedemail
    seedemail = 'madisonsocialnetworkbac@stat.wisc.edu'
    global fromname
    fromname = 'Madison Social Network'
    global message
    message = 'MS_9TYsnax2blYq8lf'
    global userid
    userid = 'asayler#uwmadison'
    global token
    token = 'yPJ1G8OxZVuGedb8n37tV1QwuHIl3YIKVDrQoWu3'
    global library
    library = 'UR_5w1mjQEYYPfJxaZ'
    global panel 
    panel = 'ML_1U1UrJb9q5WZpop'
    global survey1id 
    survey1id = 'SV_5b8eikhbZj1548t'
    global survey1questions 
    global survey1refs
    survey1questions = ['2', '3',  '4', '5',  '6']
    #Don't edit this unless you know what you're doing
    survey1refs = ['']*len(survey1questions)
    global survey2id
    global suffix
    suffix = '@gmail.com'
    #1 to allow only emails with correct suffixes, 0 to allow any email, but with the suffix being the default
    global allowOnlySuffixes
    allowOnlySuffixes = 0
    survey2id =  'SV_8ffvFqDrW2tNeh7'
    global survey2questions
    global survey2refs 
    survey2questions = ['2', '3',  '4',  '5',  '6']
    #don't edit this either unless you know what you're doing
    survey2refs = ['']*len(survey1questions)
    #only edit this if you're using a different API version 
    for i in range(0,len(survey1questions)):
       survey2refs[i] = 'q' + survey2questions[i]
       survey1refs[i] = 'q' + survey1questions[i]
    #don't use special characters in your subject for now, I'll try and add this later
    global subject 
    #Alan will change this once 
    subject = 'You have been invited to take a survey'
    global subject2
    subject2 = 'You have been invited to take a survey by '
    global fromwho 
    fromwho = 'madisonsocialnetwork@stat.wisc.edu'

    #end users: you shouldn't have to edit anything below this line
    userid = userid.replace('#', '%23')
    subject = subject.replace(' ', '%20')
    subject2 = subject2.replace(' ', '%20')
    fromname = fromname.replace(' ', '%20')
    global rooturl 
    rooturl = 'https://survey.qualtrics.com/WRAPI/ControlPanel/api.php'
    global version 
    version = '2.5'
    global form 
    form = 'XML'
    global basicurl 
    basicurl = rooturl + '?API_SELECT=ControlPanel&Version=' + version + '&Request='
    global midurl 
    midurl = '&User=' + userid + '&Token=' + token + '&Format=' + form
    fromwho = fromwho.replace('@', '%40')
    
    return
