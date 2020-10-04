import requests
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

fname='/home/pi/photo_scripts/image.jpg'

url = "https://notify-api.line.me/api/notify" 
token = os.environ.get("ENV_TOKEN")
headers = {"Authorization" : "Bearer "+ token} 

message =  "picture"
payload = {"message" :  message} 
files = {"imageFile": open(fname, "rb")} 
r = requests.post(url, headers = headers, params=payload, files=files) 
