
firstjpg=lib.googleapi .detect_web(path='config/下載.jpeg')

from google.oauth2 import service_account
import io
from google.cloud import vision
credentials = service_account.Credentials. from_service_account_file('config/api.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

def vision_api(path):
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    print(content)

a=vision_api(path='config/下載.jpeg')
a.content
