import cv2
import numpy as np

image = cv2.imread("images.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(image_gray,180,255,cv2.THRESH_BINARY)

kernel = np.ones((2, 2), np.uint8)
dilate_image = cv2.dilate(thresh, kernel)
erode_image = cv2.erode(dilate_image, kernel) 
closing = cv2.morphologyEx(erode_image, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
median_blur = cv2.medianBlur(opening, 5)

font = cv2.FONT_HERSHEY_SIMPLEX  
org = (150, 24)
fontScale = 1
color = (0, 0, 0)
thickness = 2
image_text = cv2.putText(median_blur, 'PF_1', org, font, fontScale, color, thickness)
cv2.imwrite("saved_img.jpeg", image_text)

cv2.imshow("text", image_text)
# cv2.imshow("mdeianBlur", median_blur)
# cv2.imshow("close", closing)
# cv2.imshow("open", opening)
# cv2.imshow("dilate", dilate_image)
# cv2.imshow("erode", erode_image)
# cv2.imshow("thresh", thresh)
# cv2.imshow("gray", image_gray)
cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()