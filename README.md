

---

# Volume Control Using Hand Gestures

## Introduction

Control your device's volume effortlessly using hand gestures! This project utilizes your index and thumb fingers to adjust the volume, eliminating the need for physical buttons that might fail over time.

## Requirements

- **OpenCV**: For camera access.
- **Mediapipe**: For hand tracking.
- **pyAutoGUI**: For keyboard controls.

## Procedure

1. **Copy `main.py`**: Download or copy the `main.py` script to your local machine.
2. **Adjust Distance**: Modify the distance threshold between the index and thumb fingers in the script to fit your needs.
3. **Run the Code**: Execute the script.
4. **Grant Camera Access**: Allow access to your camera when prompted.
5. **Test the Gesture**: Move your index and thumb fingers to see the volume control in action.

## Working

The script measures the distance between the index and thumb fingers. Based on this distance, it increases or decreases the device's volume. The script is designed to detect and respond to movements of a single hand.

## Uses

- Hands-free volume control
- Convenient when physical buttons are inaccessible or malfunctioning
- Innovative solution for touchless device interaction

---
