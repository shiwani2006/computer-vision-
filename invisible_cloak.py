import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    ret,current_frame = cap.read()
    if ret:
        #converting from rgb to hsv color space 
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
        
        #range for lower black
        l_black = np.array([0,0,0])
        u_black = np.array([180,255,50])
        mask1 = cv2.inRange(hsv_frame, l_black, u_black)

        #range for upper black
        l_black = np.array([0,0,50])
        u_black = np.array([180,255,90])
        mask2 = cv2.inRange(hsv_frame, l_black, u_black)

        #generating the final pink mask 
        black_mask = mask1 + mask2

        black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=10)
        black_mask = cv2.morphologyEx(black_mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)

        #subsituting the black porton with background image
        part1 = cv2.bitwise_and(background, background, mask=black_mask)

        #detecting the things that are not black
        black_free = cv2.bitwise_not(black_mask)

        #if cloak is not present show the current image
        part2 = cv2.bitwise_and(current_frame,current_frame, mask= black_free)

        #final output

        cv2.imshow("cloak", part1+part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

