import lib.googleapi as googleapi
import lib.testsample as testsample
web_detection=googleapi.annotate(testsample.pictureurl)
class pages_with_matching_images():
    def __init__(self,web_detection):
        self.pages_with_matching_images=web_detection.pages_with_matching_images

