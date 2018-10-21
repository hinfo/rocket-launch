from __future__ import print_function
import datetime
import gflags
import googleapiclient.discovery as discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google.oauth2 import service_account

#codigo para calendário



    
client_id2 = 'INSERT YOUR ID'
client_secret2 = 'INSERT YOUR SECRET'



flags = gflags.FLAGS

flow = client.OAuth2WebServerFlow(client_id2,
                           client_secret2,
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='https://rocket-launch.herokuapp.com/')


auth_uri = flow.step1_get_authorize_url()
#INSERT CODE RETURNED BY AUTH 
credentials = flow.step2_exchange(CODE)


from httplib2 import Http

http = Http()
http = credentials.authorize(http)

service = build('calendar', 'v3', http)

import re
import datetime


#TO TURN FUNCTIONAL, REDIRECT TO OUTPUT OF tw.py
twitt_input = [{'created_at': 'Sun Oct 21 18:55:01 +0000 2018', 'id_str': '1054083653536489473', 'in_reply_to_screen_name': 'None', 'text': '.@ABC7Chicago - A local man has quite the story to tell. Back in 1962 he was an electrician engineer for .@NASA. He… https://t.co/Od2uAaSFG1'},
               {'created_at': 'Sun Oct 21 18:55:28 +0000 2018', 'id_str': '1054083767382487040', 'in_reply_to_screen_name': 'None', 'text': 'RT @esaoperations: =\u3000／ ＼\n-\u3000/\u3000 \u3000\\\n． |\u3000      |\n． |  :large_blue_circle:  |\n． | @esa|\n． |   :crossed_flags:  |\n． |@Jaxa_en\n． |  二二 |\n’／|\u3000 \u3000 ||＼\n(\u3000|\u3000 \u3000 ||   )\n|二|\u3000\u3000 ||二|\n|\u3000|…'},
               {'created_at': 'Sun Oct 21 18:55:34 +0000 2018', 'id_str': '1054083790417653761', 'in_reply_to_screen_name': 'erc_m1984', 'text': '@erc_m1984 TESTEE'},
               {'created_at': 'Sun Oct 21 18:55:34 +0000 2018', 'id_str': '1054083790417653761', 'in_reply_to_screen_name': 'erc_m1984', 'text': '@erc_m1984 launch 23-10-2018 at 22:13:45 PM launch ASTROS'}]

for twitt in twitt_input:
    for k in twitt:
        print(k," ",twitt[k])
        if re.search(r'(\d+-\d+-\d+)',twitt[k]) and re.search(r'\d+:\d+:\d',twitt[k]):
            
            words = twitt['text'].split(' ')
            for word in words:
                if re.search(r'(\d+-\d+-\d+)',word):
                    data = word
                    date = datetime.datetime.strptime(data, '%d-%m-%Y')
                    #print(date.year,'-',date.month,'-',date.day,'T',hora)
                    #print("%s-%s-%s"%(str(date.year),str(date.month),str(date.day)))
                if re.search(r'\d+:\d+:\d',word):
                    hora = word
                    #print(hora)
            event = {
                'summary' : ('LANÇAMENTO',twitt['in_reply_to_screen_name']),
                'location' : 'LANÇAMENTO',
                'description' : twitt['text'],
                'start' : {
                    'dateTime' : ("%s-%s-%sT%s"%(str(date.year),str(date.month),str(date.day),hora)),
                    'timeZone' : 'GMT',
                },
                'end' :{
                    'dateTime' : ("%s-%s-%sT%s"%(str(date.year),str(date.month),str(date.day),hora)),
                    'timeZone' : 'GMT',
                },
                  'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'],
                  'attendees': [
                    {'email': 'lpage@example.com'},
                    {'email': 'sbrin@example.com'},
                    ],
                  'reminders': {
                    'useDefault': False,
                    'overrides': [{'method': 'email', 'minutes': 24 * 60},{'method': 'popup', 'minutes': 10},],
                  },
                }
event = service.events().insert(calendarId='8ca8bl7gk62g1hlg9qffttnrj4@group.calendar.google.com', body=event).execute()
print ('Event created: %s' % (event.get('htmlLink')))
