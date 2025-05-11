# 🛣️ Real-Time Object Detection with YOLOv8 – Bengaluru City Streets

> Detecting vehicles, people, and more in real-time from personally recorded footage using Python, OpenCV, and YOLOv8.

## 📽️ Project Overview

This project demonstrates real-time object detection using **YOLOv8**, applied on traffic footage filmed by me in **Bengaluru, India**. The goal is to detect and annotate various objects such as people, vehicles, etc., using cutting-edge deep learning models and export the labeled video in YOLO-style.

---

## 🧰 Tech Stack

- **Python 3.8+**
- **OpenCV**
- **Ultralytics YOLOv8 (via PyTorch)**
- **NumPy**
- **Custom Video Footage**

---

## 🗂️ Project Folder Structure

real_time_yolo/
├── video_input/ # Input traffic footage
│ └── bengaluru_street.mp4
├── output/ # Output folder
│ └── labeled_output.mp4
├── yolo_detect.py # Detection script
└── requirements.txt # Python dependencies

---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Abhaytiwari303/real-time-yolo-v8-bengaluru.git
   cd real-time-yolo-v8-bengaluru
   ## Install dependencies & run detection
   pip install -r requirements.txt
   python yolo_detect.py
   
## 📦 Output
output/labeled_output.mp4 – video labeled in real-time using YOLOv8 

## ✅ Features
Supports YOLOv8n/s/m/l/x

Real-time labeling on high-resolution videos

Adjustable confidence threshold and display options

Clean output folder organization

