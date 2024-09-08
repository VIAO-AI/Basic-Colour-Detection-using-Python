import cv2

def start_camera_feed(color_ranges):

   ‘"’
    Starts video capture from the webcam and applies colour detection on each frame.
    ‘"’

    cap = cv2.VideoCapture(0)  # 0 for the default webcam
    if not cap.isOpened():
        print(‘Error opening the camera.’)
        return

    while(True):
        ret, frame = cap.read()
        if not ret:
            print(‘Error reading a frame.’)
            break

        processed_frame, _ = detect_colors(frame, color_ranges)
        cv2.imshow(‘Real-time Colour Detection (VIAO.AI)’, processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
