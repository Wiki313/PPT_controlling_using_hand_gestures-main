# PPT Control Using Hand Gestures 🎯

Control PowerPoint presentations hands-free using real-time hand gesture recognition with OpenCV and MediaPipe.

Show an open palm to the webcam and hold it for 2 seconds to move between slides — no clicker or keyboard needed.

## Gestures

| Gesture | Action | Key Pressed |
|---------|--------|-------------|
| Right-hand open palm, held 2 seconds | Next slide | Right arrow |
| Left-hand open palm, held 2 seconds | Previous slide | Left arrow |

Press `Esc` to exit.

## Features

- Hands-free PowerPoint slide control
- Left- and right-hand gesture recognition
- Real-time hand landmark detection with MediaPipe Hands
- Works with PowerPoint via keyboard simulation with PyAutoGUI
- Live camera preview with hand landmarks

## Requirements

- Python 3.8+
- Webcam
- A PowerPoint file to present

Install dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

## How to Run

```bash
python project.py your_presentation.pptx
```

1. Place your PowerPoint file in the project directory, or pass its path as the argument.
2. The script opens the file and starts the webcam.
3. Hold your right-hand open palm for 2 seconds for the next slide, left-hand open palm for 2 seconds for the previous slide.
4. Press `Esc` to quit.

A sample file `ab.ppt` is included in this repo for testing.

## Project Structure

```text
.
├── project.py   # Main script: gesture detection and slide control
├── ab.ppt       # Sample presentation for testing
└── README.md    # Project documentation
```

## How It Works

1. OpenCV captures frames from the webcam.
2. MediaPipe Hands detects hand landmarks in real time.
3. If an open palm is detected and held for 2 seconds, a gesture command is triggered.
4. PyAutoGUI simulates a right or left arrow key press to change slides.

## Future Improvements

- Custom gesture mapping for more actions (start/stop slideshow, jump to first/last slide)
- Support for PDF viewers and other presentation software
- On-screen gesture confidence indicator

## Author

Muhammad Waqar — [LinkedIn](https://www.linkedin.com/in/mwaqar-ai/)
