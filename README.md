# 🖱️ Virtual Mouse Using AI/ML

A touchless virtual mouse system using computer vision and artificial intelligence that enables users to control their computer with hand gestures. Ideal for hygienic, contactless interaction and accessibility use cases.

---

## 🚀 Features

- 🎯 Real-time hand tracking using MediaPipe
- 🖐️ Gesture recognition for mouse actions
- 🖱️ Mouse movement, left/right click, scrolling
- ⚙️ Cross-platform support (Windows, macOS, Linux)
- 👨‍💻 Python-based, open-source, and customizable

---

## 🧠 How It Works

1. Capture video input from the webcam using OpenCV.
2. Detect hands and extract 21 hand landmarks using MediaPipe.
3. Track finger positions and identify gestures.
4. Simulate mouse events (move, click, scroll) using PyAutoGUI.

---

## 🛠️ Tech Stack

| Tool/Library    | Purpose                              |
|-----------------|--------------------------------------|
| Python          | Core programming language            |
| OpenCV          | Image processing and webcam input    |
| MediaPipe       | Real-time hand tracking              |
| PyAutoGUI       | Mouse and keyboard automation        |
| NumPy           | Numerical operations and arrays      |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Paarth01/Virtual-Mouse-Using-AI-ML.git
cd Virtual-Mouse-Using-AI-ML
```
### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python virtual_mouse.py
```

## 🎮 Gesture Controls

| Gesture               | Action      |
| --------------------- | ----------- |
| Index finger only     | Move cursor |
| Index + thumb (pinch) | Left click  |
| Closed fist           | Right click |
| Two fingers up        | Scroll      |

## 📁 Project Structure

```bash
Virtual-Mouse-Using-AI-ML/
├── virtual_mouse.py         # Main application file
├── HandTrackingModule.py    # Hand detection and gesture logic
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## 🔮 Future Enhancements

- Trainable gesture recognition using machine learning
- Voice command integration
- GUI overlay for visual feedback on gesture recognition
- Adaptive cursor control sensitivity
- Gesture-controlled volume, brightness, etc.

## 🤝 Contributing

Contributions are welcome! Feel free to:
-⭐ Star this repository
-📂 Fork it and create your feature branch
-📥 Submit pull requests
-📧 Open issues and share feedback

## 📜 License
This project is licensed under the MIT License.

