# Calibrate dji tello camera with arUco markers using opencv and python. 
(Code developed and tested on opencv 3.3.1)
# what is Dji Tello drone:
Tello is a small quadcopter that features a Vision Positioning System and an onboard camera.

# Notable Features of Tello Drone
DJI Tello has an excellent flight time of 13 minutes. (enough for your indoor testing!)
It comes with a 5MP camera. It can shoot 720p videos, and has digital image stabilization!
Approximately 80 g (Propellers and Battery Included) in weight.
This small drone has a maximum flight distance of 100 meters and you can fly
The Tello drone is equipped with a camera that has the following intrinsic parameters:

Focal length (fx, fy): 3.58mm
Optical center (cx, cy): (960, 540)
Image resolution: 960x720 pixels

These intrinsic parameters are fixed and cannot be changed. However, it is possible to adjust the camera's field of view and perspective through software settings in the Tello app or programming interface.

# camera_calibration
Code and resources for camera calibration using arUco markers and opencv 

1. Print the aruco marker board provided. (You can generate your own board, see the code "camera_calibration.py")
2. Take around 50 images of the printed board pasted on a flat card-board, from different angles. Use Use data_generation_tello_camera or data_generation_laptop_camera  node for this based on your need.
3. Set path to store images first.
4.refer to /aruco_images for sample pictures
5.make sure you move the board along 3 axis ,X,Y,Z

In my case,I took 120 photos but it depends on the user


## Calibrating camera
make it executable and run the file "camera_calibration.py" 
'''
1.chmod +x camera_calibration.py
2.python camera_calibration.py
'''




