Here’s a **`README.md`** file for PPT_controlling_using_hand_gestures-main

---

```markdown
# PPT Control Using Hand Gestures 🎯

This project allows you to control **PowerPoint presentations** using **hand gestures** with the help of **OpenCV** and **MediaPipe**.  
You can move to the **next** or **previous** slide by showing specific hand gestures to the webcam.

## 🚀 Features
- Hands-free PowerPoint slide control.
- Recognizes **left and right-hand gestures** for navigation.
- Uses **MediaPipe Hands** for gesture detection.
- Works with any presentation software (PowerPoint, PDF Viewer, etc.) using `pyautogui`.

## 📂 Project Structure
```

robot\_controlling\_using\_hand\_gestures-main/
│
├── project.py   # Main script for gesture detection & slide control
└── README.md    # Project documentation

````

## 🛠️ Requirements
Install the following Python libraries:
```bash
pip install opencv-python mediapipe pyautogui
````

## ▶️ How to Run

1. Place your PowerPoint file in the project directory.
2. Run the script with your file name:

   ```bash
   python project.py your_presentation.pptx
   ```
3. Use your **right hand** to move to the **next slide** and your **left hand** to move to the **previous slide**.

## 🧠 How It Works

* **MediaPipe Hands** detects your hand landmarks in real-time.
* If an open palm is detected and held for **2 seconds**, a gesture command is triggered.
* **PyAutoGUI** simulates keyboard arrow key presses to control slides.

## 🔧 Future Improvements

* Add custom gesture mapping for more actions (start/stop slideshow).
* Support multiple gesture-based commands.
* Extend functionality for hardware integration.

## ✨ Demo

* **Right Hand** ➡ Next Slide
* **Left Hand** ⬅ Previous Slide

---

**Author:** Waqar Afridi

```

---

Would you like me to **generate this `README.md` file** and give you a **ready-to-download version**?
```

