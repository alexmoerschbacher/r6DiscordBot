from datetime import datetime
from dateutil import parser
import os
from requests import post
import json
from dotenv import load_dotenv
class Auth:
    def getAuth(self) -> 'AuthResponse':
        if os.path.exists('auth.json'):
            jsonObject = json.load(open('auth.json', 'r'))
            expirationTime = parser.parse(jsonObject['expiration'])
            timezone = expirationTime.tzinfo
            if  expirationTime > datetime.now(timezone):
                return AuthResponse("ubi_v1 t=" + jsonObject["ticket"], jsonObject["expiration"], jsonObject["sessionId"], jsonObject["spaceId"])
                
        load_dotenv()
        headers = {
            'Authorization': os.getenv('AUTHORIZATION'),
            'Ubi-AppId': '39baebad-39e5-4552-8c25-2c9b919064e2',
            'Content-Type': 'application/json'
        }
        response = post("https://public-ubiservices.ubi.com/v3/profiles/sessions", headers=headers)
        response = response.json()
        with open('auth.json', 'w') as outfile:
            json.dump(response, outfile)
        return AuthResponse("ubi_v1 t=" + response["ticket"], response["expiration"], response["sessionId"], response["spaceId"])



class AuthResponse:
    def __init__(self, authorization, expiration, sessionId, spaceId):
        self.authorization = authorization
        self.expiration = expiration
        self.sessionId = sessionId
        self.spaceId = spaceId