import freenect #check if freenect is installed system wide
import cv2
import numpy as np
import threading

def get_video():
    while True:
        array, _ = freenect.sync_get_video()
        frame = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        cv2.imshow('Kinect Video Feed', frame)
        if cv2.waitKey(1) == 27:
            break
if __name__ == "__main__":
    video_thread = threading.Thread(target=get_video)
    video_thread.start()
    video_thread.join()
    cv2.destroyAllWindows()
