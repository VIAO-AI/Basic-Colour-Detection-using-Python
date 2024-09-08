from color_detection.utils import detect_colors
from color_detection.visualization import display_results
from color_detection.config import COLOR_RANGES
from color_detection.camera_feed import start_camera_feed


def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image '{image_path}'")
        return

    colored_image, contours = detect_colors(image, COLOR_RANGES)
    display_results(colored_image, contours)


if __name__ == "__main__":
  
    # User options:
  
    option = input("Do you want to process an image or use the camera? (i/c):")

    if option.lower() == 'i':
        image_path = input("Enter the path to the image: ")
        process_image(image_path)
    elif option.lower() == 'c':
        start_camera_feed(COLOR_RANGES)  # Start video capture
    else:
        print("Invalid option.")
