import io
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
import json

class Api:
    def __init__(self, key_file = 'ADDecter/config/key.json'):
        credentials = service_account.Credentials.from_service_account_file(key_file)
        self.client = vision.ImageAnnotatorClient(credentials=credentials)
    
    def image_processing(self, image_path):
        if image_path.startswith('http') or image_path.startswith('gs:'):
            image = types.Image()
            image.source.image_uri = image_path
        else: 
            with io.open(image_path, 'rb') as image_file:
                content = image_file.read()
            image = types.Image(content=content) 
        return image

    def face(self, image_path):
        image = self.image_processing(image_path)
        face = self.client.face_detection(image=image)
        return face

    def lables(self, image_path):
        image = self.image_processing(image_path)
        lable = self.client.label_detection(image=image)
        return lable

    def logo(self, image_path):
        image = self.image_processing(image_path)
        logo = self.client.logo_detection(image=image)
        return logo

    def landmark(self, image_path):
        image = self.image_processing(image_path)
        landmark = self.client.landmark_detection(image=image)
        return landmark

    def text(self, image_path):
        image = self.image_processing(image_path)
        text = self.client.text_detection(image=image)
        return text

    def properties(self, image_path):
        image = self.image_processing(image_path)
        properties = self.client.image_properties(image=image)
        return properties

    def safe_properties(self, image_path):
        image = self.image_processing(image_path)
        safe_properties = self.client.safe_search_detection(image=image)
        return safe_properties

    def web_entities(self, image_path):
        image = self.image_processing(image_path)
        web_entities = self.client.web_detection(image=image)
        return web_entities

    def document_text(self, image_path):
        image = self.image_processing(image_path)
        document_text = self.client.document_text_detection(image=image)
        return document_text

    def objects(self, image_path):
        image = self.image_processing(image_path)
        objects = self.client.object_localization(image=image)
        return objects

    def crop_hints_params(self, image_path):
        image = self.image_processing(image_path)
        crop_hints_params = vision.types.CropHintsParams(aspect_ratios=[1.77])
        image_context = vision.types.ImageContext(
            crop_hints_params=crop_hints_params)
        crop = self.client.crop_hints(image=image, image_context=image_context)
        hints = crop.crop_hints_annotation.crop_hints
        # Get bounds for the first crop hint using an aspect ratio of 1.77.
        vertices = hints[0].bounding_poly.vertices
        return vertices