# 🖐️ Hand Tracking & Gesture Volume Control System

A real-time computer vision project built using Python, OpenCV, and MediaPipe that tracks hand movements and controls system volume through hand gestures.

## 🚀 Features

* Real-time hand tracking using webcam
* Detection of hand landmarks and finger positions
* Gesture-based system volume control
* Smooth hand movement recognition
* FPS display for performance monitoring
* Interactive visual feedback with tracking points and connections

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* CV2
* Math Libraries

## 📌 How It Works

The project uses MediaPipe Hands to detect and track hand landmarks in real time.
By calculating the distance between the thumb and index finger, the program dynamically adjusts the system volume.

### Gesture Logic

* Fingers close together → Lower volume
* Fingers far apart → Higher volume

The hand landmarks are continuously processed using OpenCV for live visualization and interaction.

## 📂 Project Structure

```bash
├── HandTracking.py
├── volumehandtracking.py
├── HandTrackingModule.py
└── README.md
```

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Install dependencies:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

Run the project:

```bash
python volumehandtracking.py
```

## 🎯 Future Improvements

* Gesture-based media controls
* Virtual mouse using hand tracking
* Brightness control through gestures
* Multi-hand interaction support
* AI-based gesture recognition

## 📸 Output

Real-time webcam visualization with:

* Hand landmark detection
* Finger tracking
* Gesture recognition
* Dynamic volume adjustment

## 💡 Learning Outcomes

This project helped in understanding:

* Computer Vision fundamentals
* Real-time image processing
* Gesture recognition systems
* Human-computer interaction
* MediaPipe hand landmark detection

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper attribution.

---

⭐ If you like this project, consider giving it a star on GitHub!
