import cv2
import numpy as np

def detect_colors(image, color_ranges):
  """
  Detecta colores definidos en 'color_ranges' en una imagen y devuelve la imagen con los contornos dibujados y los contornos encontrados.

  **Objetivo:** Enseñar a la computadora a "ver" como nosotros, identificando colores específicos. 
  **Pasos:**
    1. **Convertir la imagen:** La imagen se convierte al espacio de color HSV para facilitar la detección de colores.
    2. **Crear máscaras:** Para cada color, se crea una máscara que resalta solo las zonas con ese color.
    3. **Encontrar contornos:** Se buscan los bordes de las zonas de color en las máscaras.
    4. **Dibujar contornos:** Los contornos encontrados se dibujan en la imagen original.
  """

  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  contours_list = []
  for color_name, (lower, upper, color) in color_ranges.items():
      mask = cv2.inRange(hsv, lower, upper)
      contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(image, contours, -1, color, 3) 
      contours_list.append(contours)

  return image, contours_list 