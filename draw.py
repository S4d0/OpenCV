import numpy as np
import cv2 as cv

# Create a black image 
img = np.zeros((512,512,3), np.uint8) 

# Draw 2 diagonal blue line with 2 px thickness
# cv2.line function = source image, line start point, line end point, color, thickness
cv.line(img, (0,0),   (511,511), (255,0,0), 5) 
cv.line(img, (0,511), (511,0),   (255,0,0), 5)

# Adding text to images
# cv2.putText function = source image, text to be drawn, bottom left of text, font, size, color, thickness, line type
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (90,70)  , font, 3, (255,255,255), 2, cv.LINE_AA)
cv.putText(img, 'S4d0'  , (120,500), font, 4, (255,255,255), 2, cv.LINE_AA)

# Shows the image
cv.imshow("image", img)

# If user press to s key, saves the image and close the program, otherwise just close the program
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("helloOpenCV.png", img)
