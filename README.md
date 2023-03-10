# Calibrate dji tello camera with arUco markers using opencv and python. 
(Code developed and tested on opencv 3.3.1)


# camera_calibration
Code and resources for camera calibration using arUco markers and opencv 

1. Print the aruco marker board provided. (You can generate your own board, see the code "camera_calibration.py")
2. Take around 50 images of the printed board pasted on a flat card-board, from different angles. Use Use data_generation_tello_camera or data_generation_laptop_camera  node for this based on your need.
3. Set path to store images first.
4.refer to /aruco_images for sample pictures
5.make sure you move the board along 3 axis ,X,Y,Z

In my case,I took 120 photos but it depends on the user


## Calibrating camera
run the file "camera_calibration.py" after you make it executable with " chmod +x camera_calibration.py "



