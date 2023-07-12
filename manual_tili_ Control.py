import freenect
import signal
import cv2

tilt_angle = 0

def adjust_tilt(dev):
    global tilt_angle
    freenect.set_tilt_degs(dev, tilt_angle)

def on_trackbar(value):
    global tilt_angle
    tilt_angle = value - 30  
    adjust_tilt(dev)

def handler(signum, frame):
    print('Stopping...')
    freenect.sync_stop()

if __name__ == "__main__":
    ctx = freenect.init()
    dev = freenect.open_device(ctx, 0) 
    signal.signal(signal.SIGINT, handler)
    cv2.namedWindow("Tilt Control")
    cv2.createTrackbar("Tilt Angle", "Tilt Control", 30, 60, on_trackbar)
    while True:
        print("Current tilt angle:", tilt_angle)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    freenect.close_device(dev)
    freenect.shutdown(ctx)
