#!/usr/bin/python

import httplib2
import pprint
python 
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow


# Copy your credentials from the console
CLIENT_ID = '602014705145-3dj3g5970c4idbu9v0e7k1n1geacl2uq.apps.googleusercontent.com'
CLIENT_SECRET = 'WLknjvwNmr8cmncPHeYIOalC'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'My document',
  'description': 'A test document',
  'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)
