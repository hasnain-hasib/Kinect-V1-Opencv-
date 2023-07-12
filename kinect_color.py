import freenect
import cv2
import numpy as np
import threading


latest_frame = None
latest_depth = None
object_position = (0, 0)
deep_purple_lower = (130, 50, 50)
deep_purple_upper = (160, 255, 255)

def get_video():
    global latest_frame
    while True:
        array, _ = freenect.sync_get_video()
        frame = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        latest_frame = frame

def get_depth():
    global latest_depth
    while True:
        array, _ = freenect.sync_get_depth()
        depth = array.astype(np.float32) * 0.1
        latest_depth = depth


def detect_objects():
    global object_position
    while True:
        if latest_frame is not None and latest_depth is not None:
            hsv_frame = cv2.cvtColor(latest_frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_frame, deep_purple_lower, deep_purple_upper)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)
                object_position = (x + w // 2, y + h // 2)
            else:
                object_position = (0, 0)
def display_frames():
    while True:
        if latest_frame is not None and latest_depth is not None:
            frame_with_info = latest_frame.copy()
            cv2.circle(frame_with_info, object_position, 5, (0, 255, 0), -1)
            object_depth = latest_depth[object_position[1], object_position[0]]
            cv2.putText(frame_with_info, "Distance: {:.2f} cm".format(object_depth),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame_with_info, "Position: {}".format(object_position),
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow('Object Detection', frame_with_info)
        if cv2.waitKey(1) == 27:
            break

if __name__ == "__main__":
    video_thread = threading.Thread(target=get_video)
    depth_thread = threading.Thread(target=get_depth)
    detection_thread = threading.Thread(target=detect_objects)
    display_thread = threading.Thread(target=display_frames)
    video_thread.start()
    depth_thread.start()
    detection_thread.start()
    display_thread.start()
    display_thread.join()
    video_thread.join()
    depth_thread.join()
    detection_thread.join()

    cv2.destroyAllWindows()
