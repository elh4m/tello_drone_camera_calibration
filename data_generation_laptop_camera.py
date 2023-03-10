'''I wrote This script is for generating data from laptop camera and has the ability to save the images inside the desired path
1. Provide desired path to store images.
2. Press 'c' to capture image and display it.
4. Press 'q' to quit.
'''
import os
import cv2

camera = cv2.VideoCapture(0)
ret,img = camera.read()

path = "calibration_aruco/camera_calibration/aruco_images/"
count = 0

def save_image(img, name):
    cv2.imwrite(name, img)
    print(f"Image saved as {name}")

while True:
    name = path + str(count)+".jpg"
    name=os.path.join(os.path.expanduser('~'),name)
    ret, img = camera.read()
    cv2.imshow("img", img)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        save_image(img, name)
        count += 1
    elif cv2.waitKey(20) & 0xFF == ord('q'):
        break;

camera.release()
cv2.destroyAllWindows()

