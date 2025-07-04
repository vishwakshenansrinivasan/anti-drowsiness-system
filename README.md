# 💤 Anti-Drowsiness Detection System

A real-time eye-based driver drowsiness detection system using OpenCV, dlib, and Python. The system monitors the user's eye aspect ratio (EAR) using facial landmarks and triggers an audio + desktop notification alert when prolonged eye closure is detected—indicating drowsiness.

---

## 📸 How It Works

- Uses **dlib’s 68 facial landmarks model** to detect and track eyes.
- Computes **Eye Aspect Ratio (EAR)** to determine whether eyes are open or closed.
- If EAR stays below a threshold for a continuous number of frames, it assumes the user is drowsy.
- Triggers:
  - **Alarm sound** (using `pygame`)
  - **System desktop notification** (using `plyer`)

---

## ✅ Features

- Real-time face and eye detection
- EAR (Eye Aspect Ratio) calculation for blink/drowsiness monitoring
- Visual feedback via OpenCV (live EAR and alert overlay)
- Plays alarm (`alarm.mp3`) and shows desktop notification if drowsy
- Lightweight and suitable for laptops or embedded devices with webcam

---

## 📂 Project Structure

```
.
├── shape_predictor_68_face_landmarks.dat   # Pretrained facial landmark model (required)
├── alarm.mp3                               # Alarm audio file (add your own if needed)
├── drowsiness_detector.py                  # Main Python script
```

---

## ⚙️ Requirements

- Python 3.7+
- OpenCV
- dlib
- numpy
- pygame
- scipy
- plyer

---

## 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishwakshenansrinivasan/anti-drowsiness-system.git
   cd anti-drowsiness-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the facial landmark model**

   Download `shape_predictor_68_face_landmarks.dat` from:
   [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

   Extract and place it in the project directory.

4. **Ensure alarm file is present**

   Add a file named `alarm.mp3` in the project folder. You can use any short loud alarm sound.

---

## ▶️ Usage

Run the script:
```bash
python drowsiness_detector.py
```

- Press **Q** to exit the application.
- A red screen + alarm + notification appear if drowsiness is detected.

---

## 🔍 Detection Logic

- **EAR Threshold**: `0.25`
- **Frames before alarm**: `20` continuous frames below threshold
- EAR is calculated as:

  \[
  EAR = rac{||p2 - p6|| + ||p3 - p5||}{2 \cdot ||p1 - p4||}
  \]

- If EAR < threshold for 20 consecutive frames → **Drowsiness Alert**

---

## 🧪 Sample Output

- Live EAR display on screen
- "ALERT! DROWSINESS DETECTED" overlay if drowsy
- Red screen tint + alarm + system notification

---

## 📌 Notes

- Make sure your webcam is enabled and accessible.
- Lighting conditions may affect face detection accuracy.
- Works best when user is facing the camera frontally.

---

## 🛠️ To-Do / Improvements

- Add logging of drowsiness events
- Enable email/SMS alert
- Train and use a CNN model for more robust eye state classification
- Improve support for multiple users or sunglasses

---

## 🙌 Acknowledgements

- [dlib](http://dlib.net/) for facial landmark detection
- [Tereza Soukupova & Jan Cech](https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf) – EAR concept
- [plyer](https://github.com/kivy/plyer) – cross-platform desktop notifications

---

## 👤 Author

- **Vishwakshenan Srinivasan**  
- GitHub: [@vishwakshenansrinivasan](https://github.com/vishwakshenansrinivasan)

---

🚗 **Drive safe. Rest well. Stay alert.**
