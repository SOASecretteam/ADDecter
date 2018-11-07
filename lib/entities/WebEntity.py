import lib.gateways.googleapi as googleapi
import lib.gateways.testsample as testsample

class WebEntity():
    def __init__(self,web_detection):
        self.webentities=web_detection.web_entities
