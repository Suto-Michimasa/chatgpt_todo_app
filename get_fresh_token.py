from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import os
import json

# サービス名、スコープ、クレデンシャル情報を指定
SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """ユーザーの認証情報を取得する"""
    # 認証情報のファイルが存在するかチェック
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
        credential_dir, 'calendar-python-quickstart.json')

    # ストアされた認証情報をロード
    credentials = None
    if os.path.exists(credential_path):
        with open(credential_path, 'r') as f:
            credentials = Credentials.from_authorized_user_info(json.load(f))

    # ストアされた認証情報が有効でない場合は、新しい認証情報を作成して取得します。
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # 取得した認証情報をストア
        with open(credential_path, 'w') as f:
            f.write(credentials.to_json())

    return credentials


get_credentials()
