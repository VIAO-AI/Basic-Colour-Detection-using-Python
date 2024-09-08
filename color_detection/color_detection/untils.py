import cv2
import numpy as np

def detect_colors(image, color_ranges):
  """
  Detects colours defined in ‘colour_ranges’ in an image and returns the image with the contours drawn and the contours found.
  
  **Objective:** To teach the computer to ‘see’ as we do, identifying specific colours. 
  **Steps
    1. **Convert the image:** The image is converted to the HSV colour space to facilitate colour detection.
    2. **Create masks:** For each colour, a mask is created that highlights only the areas with that colour.
    3. **Find outlines:** The edges of the colour areas in the masks are searched for.
    4. **Draw contours:** The contours found are drawn on the original image.
  ‘"’

  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  contours_list = []
  for color_name, (lower, upper, color) in color_ranges.items():
      mask = cv2.inRange(hsv, lower, upper)
      contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(image, contours, -1, color, 3) 
      contours_list.append(contours)

  return image, contours_list 
