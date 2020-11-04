# Prashant Sharma Invisible Cloak. Harry Potter style
# Importing libraries

import numpy as np 
import cv2
import time
print ("Invisible Cloak By Prashant Sharma")

#Capturing WebCam Feed
cap=cv2.VideoCapture(0)

# give the camera to warm up 
time.sleep(2)  

background = 0 

#Capturing background
for i in range(30): 
    ret, background = cap.read() 
    if ret == False : 
        continue

while (cap.isOpened()):
     ret, img = cap.read()
     if not ret:
         break;
     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     lower_red = np.array([0, 120, 70])        
     upper_red = np.array([10, 255, 255])
     mask1 = cv2.inRange(hsv, lower_red, upper_red) #Separating the cloak

     lower_red = np.array([170, 120, 70]) 
     upper_red = np.array([180, 255, 255]) 
     mask2 = cv2.inRange(hsv, lower_red, upper_red)

     mask1 = mask1 + mask2

# Refining the mask corresponding to the detect red color 
     mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), 
                                         np.uint8), iterations = 2) #noise removal
     mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), 
                                         np.uint8), iterations = 1)
     mask2 = cv2.bitwise_not(mask1) 

# Generating the final output 
     res1 = cv2.bitwise_and(background, background, mask = mask1) 
     res2 = cv2.bitwise_and(img, img, mask = mask2) 
     final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

     cv2.imshow("Invisible Cloak By Prashant Sharma", final_output) 
     k = cv2.waitKey(10) 
     if k == 27: 
        break

cap.release()
cv2.destroyAllWindows()