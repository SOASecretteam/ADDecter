import io 
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types

#authorize
credentials = service_account.Credentials.from_service_account_file('C:/Users/Lynn/Desktop/SOA/key.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

def annotate(path):
    """Returns web annotations given the path to an image."""
    if path.startswith('http') or path.startswith('gs:'):
        image = types. Image()
        image.source.image_uri = path
    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
    web_detection = client.web_detection(image=image).web_detection
    return web_detection

annotate(file_name)