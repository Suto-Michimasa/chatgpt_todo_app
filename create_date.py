import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import os

# Google APIクライアントの作成
SCOPES = ['https://www.googleapis.com/auth/calendar']
PATH = 'token.json'
calender_Id = 'suto.michimasa.work@gmail.com'

creds = Credentials.from_authorized_user_file(PATH, SCOPES)
service = build('calendar', 'v3', credentials=creds)

# イベントのパラメータを指定する
event = {
    'summary': '研究室のMTG',
    'location': '研究室',
    'start': {
        'dateTime': '2023-04-12T10:00:00+09:00',
        'timeZone': 'Asia/Tokyo',
    },
    'end': {
        'dateTime': '2023-04-12T12:00:00+09:00',
        'timeZone': 'Asia/Tokyo',
    },
    'reminders': {
        'useDefault': True,
    },
}

# イベントの作成
try:
    event = service.events().insert(
        calendarId=calender_Id, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
except HttpError as error:
    print('An error occurred: %s' % error)
