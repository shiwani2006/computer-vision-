# Invisible Cloak using Python + OpenCV

This project recreates the popular **Invisible Cloak Effect** using Python and OpenCV. By detecting a specific color in the video feed and replacing it with a captured background, the selected area becomes invisible — giving a fun Harry Potter–style disappearing effect!

## 🎯 Project Overview

This script identifies a predefined color range in the HSV color space. Wherever the selected color appears, that region is replaced by the background image, creating the illusion of invisibility.

## 🧠 What You’ll Learn

* Color detection using **HSV**
* Creating and applying **background masks**
* Working with **real-time video processing**
* Basic **image segmentation** techniques
* Understanding a simple **computer vision workflow**

## 🚀 Why I Made This

I wanted to explore computer vision with a project that’s simple yet exciting. This turned out to be a great hands-on introduction and motivated me to dive deeper into advanced AI/ML concepts.

## 📌 Requirements

* Python 3.x
* OpenCV (`pip install opencv-python`)
* NumPy (`pip install numpy`)
* Webcam

## ▶️ How to Run

1. Capture or choose a background image.
2. Run the script.
3. Wear or hold an object of the target color (e.g., red cloth).
4. Watch the invisible cloak effect appear in real time.

## 📁 Features

* Real-time detection
* Smooth masking and blending
* Beginner-friendly code structure

## 🙌 Future Improvements

* Multi-color cloak detection
* Better segmentation using Morphological operations
* Option to toggle cloak colors live

---

Feel free to fork this repository and experiment with new CV ideas!
