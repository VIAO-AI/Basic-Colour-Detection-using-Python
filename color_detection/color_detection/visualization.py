import cv2

def display_results(image, contours):
  
  ‘Displays the image with the detected contours.
  
  cv2.imshow(‘VIAO.AI Colour Detection’., image)
  cv2.waitKey(0)
  cv2.destroyAllWindows() 
