@author: DarkMarksDoe
"""

import cv2
 
# Black and White (gray scale)
 
Img = cv2.imread ('URLIMAGE',0)
 
cv2.imshow('Penguins', Img)
 
cv2.waitKey(0)
 
# cv2.waitKey(2000)
 
cv2.destroyAllWindows()
