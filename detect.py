from deepstack_sdk import Detection,ServerConfig
import os

config = ServerConfig("http://localhost:80")
detector = Detection(config=config, name="dark")

detections = detector.detectObject(image=os.path.join("images", "image.jpg"), output=os.path.join("images", "image_detected.jpg"))

for detection in detections:
    print("Name: {}".format(detection.label))
    print("Confidence: {}".format(detection.confidence))
    print("x_min: {}".format(detection.x_min))
    print("x_max: {}".format(detection.x_max))
    print("y_min: {}".format(detection.y_min))
    print("y_max: {}".format(detection.y_max))
    print("-----------------------")