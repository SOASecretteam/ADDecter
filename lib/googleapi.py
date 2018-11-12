import io
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
import json

#authorize
credentials = service_account.Credentials.from_service_account_file('C:/Users/Lynn/Desktop/SOA/key.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

class Api:
    def __init__(self, key_file = '/config/key.json'):
        credentials = service_account.Credentials.from_service_account_file(key_file)
        client = vision.ImageAnnotatorClient(credentials=credentials)

def image_processing(path):
    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path
    else: 
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content) 
    return image

def face(image_path):
    image = image_processing(image_path)
    face = client.face_detection(image=image)
    return face

def lables(image_path):
    image = image_processing(image_path)
    lable = client.label_detection(image=image)
    return lable

def logo(image_path):
    image = image_processing(image_path)
    logo = client.logo_detection(image=image)
    return logo

def landmark(image_path):
    image = image_processing(image_path)
    landmark = client.landmark_detection(image=image)
    return landmark

def text(image_path):
    image = image_processing(image_path)
    text = client.text_detection(image=image)
    return text

def properties(image_path):
    image = image_processing(image_path)
    properties = client.image_properties(image=image)
    return properties

def safe_properties(image_path):
    image = image_processing(image_path)
    safe_properties = client.safe_search_detection(image=image)
    return safe_properties

def web_entities(image_path):
    image = image_processing(image_path)
    web_entities = client.web_detection(image=image)
    return web_entities

def document_text(image_path):
    image = image_processing(image_path)
    document_text = client.document_text_detection(image=image)
    return document_text

def objects(image_path):
    image = image_processing(image_path)
    objects = client.object_localization(image=image)
    return objects

def crop_hints_params(image_path):
    image = image_processing(image_path)
    crop_hints_params = vision.types.CropHintsParams(aspect_ratios=[1.77])
    image_context = vision.types.ImageContext(
        crop_hints_params=crop_hints_params)
    crop = client.crop_hints(image=image, image_context=image_context)
    hints = crop.crop_hints_annotation.crop_hints
    # Get bounds for the first crop hint using an aspect ratio of 1.77.
    vertices = hints[0].bounding_poly.vertices
    return vertices

# compute the outputs
crop = objects(uri)

# write to json file
with open("file.json", 'w') as fjs:
    fjs.write(MessageToJson(crop))