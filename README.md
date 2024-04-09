
## Kinect Object Detection

This repository contains two Python scripts that demonstrate object detection using the Kinect sensor.

### Dependencies

- [OpenKinect](https://openkinect.org/): A library for accessing the Kinect sensor.
- [OpenCV](https://opencv.org/): An open-source computer vision library.

### Code Snippets

1. `tilt_control.py`: This script allows you to control the tilt angle of the Kinect sensor using a trackbar in a graphical user interface (GUI) window. It uses the `freenect` library to interact with the Kinect sensor and the `cv2` library for GUI and trackbar functionality.

2. `object_detection.py`: This script performs object detection using the Kinect sensor. It captures RGB video and depth data from the Kinect and applies color-based segmentation to detect objects of a specific color range. The detected object's position and depth are displayed in real-time on the video feed. It uses the `freenect` and `cv2` libraries for sensor interaction and image processing.


2. Install the dependencies:

- OpenKinect: Follow the installation instructions provided in the [OpenKinect repository](https://github.com/OpenKinect/libfreenect).
- OpenCV: Install OpenCV using the package manager or follow the installation instructions for your operating system on the [OpenCV website](https://opencv.org/).

3. Run the scripts:

- For tilt control:

```
python tilt_control.py
```

- For object detection:

```
python object_detection.py
```

### Notes

- Make sure you have a Kinect sensor connected to your computer before running the scripts.
- Adjust the code as needed to match your Kinect sensor's index or other specifications.
