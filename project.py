import cv2
import mediapipe as mp
import time
import pyautogui
import subprocess
import sys

# Function to open the PowerPoint file
def open_powerpoint(filepath):
    if sys.platform == "win32":
        os.startfile(filepath)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", filepath])
    else:
        subprocess.Popen(["xdg-open", filepath])

# Specify the PowerPoint file
# filename = "abc.ppt"
filename = sys.argv[1]

# Open the PowerPoint file
open_powerpoint(filename)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Constants
GESTURE_DISPLAY_TIME = 2  # Seconds to hold palm to trigger gesture

# Variables for gesture detection
gesture_start_time = None

# Slide control
current_slide = 0

def move_to_next_slide():
    global current_slide
    current_slide += 1
    print(f"Moved to next slide: {current_slide}")
    pyautogui.press('right')  # For PowerPoint
    # pyautogui.press('pagedown')  # For PDF viewer

def move_to_previous_slide():
    global current_slide
    current_slide = max(0, current_slide - 1)
    print(f"Moved to previous slide: {current_slide}")
    pyautogui.press('left')  # For PowerPoint
    # pyautogui.press('pageup')  # For PDF viewer

# Video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Determine if the hand is left or right
            label = handedness.classification[0].label
            if label == "Left":
                hand_side = "left"
            else:
                hand_side = "right"

            # Get coordinates of landmarks for gesture recognition
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            # Check if palm is shown for GESTURE_DISPLAY_TIME seconds
            if (index_finger_tip.y < index_finger_mcp.y and
                middle_finger_tip.y < index_finger_mcp.y and
                pinky_tip.y < index_finger_mcp.y):  # Palm is open
                if gesture_start_time is None:
                    gesture_start_time = time.time()
                elif time.time() - gesture_start_time >= GESTURE_DISPLAY_TIME:
                    if hand_side == "right":
                        move_to_next_slide()
                    elif hand_side == "left":
                        move_to_previous_slide()
                    gesture_start_time = None  # Reset the start time for next gestures
            else:
                gesture_start_time = None  # Reset if the palm is not shown

            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the image
    cv2.imshow('Slide Controller', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
