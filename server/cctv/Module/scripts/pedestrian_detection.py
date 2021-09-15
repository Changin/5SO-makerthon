import cv2
import os

def read_image(input_path, is_resized=False):

    #IMREAD_COLOR : 3 channel, BGR
    image = cv2.imread(input_path, cv2.IMREAD_COLOR)
    if is_resized:
        image = image.resize(640, 360, interpolation=cv2.INTER_AREA)

    return image
    
def write_image(input_path, output_path, image):
    cv2.imwrite(os.path.join(output_path, os.path.basename(input_path)), image) 

def pedestrian_detection(input_path, output_path):

    _winStride = (4, 4)
    _scale = 1.1

    image = read_image(input_path, False)
    
    #cv2.imshow("test", image)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    detected, _ = hog.detectMultiScale(image, winStride=_winStride, scale=_scale)

    squares = [((x, y), (x + w, y + h)) for x, y, w, h in detected]
    for x, y, w, h in detected:
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
	
    #cv2.imshow("test", image)
    
    #write_image(input_path, output_path, image)
    
    cv2.imwrite(output_path, image)
    
def main(input_path, output_path):
    pedestrian_detection(input_path, output_path)
    
if __name__=="__main__":
    main("../examples/demo/Copy of standing_153.jpg", "../examples/res/test.jpg")
