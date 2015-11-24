
def init():
    #end users: edit the variables below this line, but above the line where
    #I tell you to stop
    global userid
    userid = 'asayler#uwmadison'
    global token
    token = 'HPByHJzIu1CBnvzsBVHkUdrjzKWtk8DdPXqqYhw3'
    global library
    library = 'UR_5w1mjQEYYPfJxaZ'
    global panel 
    panel = 'ML_aghkJBrVFyPUR6J'
    global survey1id 
    surveyid = 'SV_56ZOhUEkJS3DO4t'
    global survey1questions 
    survey1questions = ['QID31', 'QID32',  'QID33', 'QID34',  'QID35']
    global survey2id 
    survey2id =  'SV_etZ47eFodfWMFtH'
    global survey2questions 
    survey2questions = [' QID20', 'QID21',  'QID22',  'QID24',  'QID25'] 
    #don't use special characters in your subject for now, I'll try and add this later
    global subject 
    subject = 'You have been invited to take a survey'
    global fromwho 
    fromwho = 'asayler@wisc.edu'

    #end users: you shouldn't have to edit anything below this line
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
    userid = userid.replace('#', '%23')
    return
