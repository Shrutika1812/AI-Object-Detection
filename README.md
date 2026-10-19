Real-Time AI Object Detection System

A real-time computer vision application that detects and identifies everyday objects through a webcam using **Python, OpenCV, and YOLO**.

## Overview

This project uses a pretrained YOLO object detection model to identify objects in live video frames. Detected objects are displayed with bounding boxes and class labels, making the results easy to visualize.

Built as a hands-on project to explore real-time object detection and practical AI integration.

## Features

- **Live Detection:** Detects objects directly from a webcam feed.
- **Object Classification:** Displays labels for recognized objects.
- **Bounding Boxes:** Highlights detected objects visually.
- **Real-Time Visualization:** Displays annotated video frames using OpenCV.
- **Simple Execution:** Runs locally with a single Python command.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Ultralytics YOLO | Object detection model |
| OpenCV | Webcam access and visual output |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
AI-Object-Detection/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python installed
- A working webcam
- Internet access for the initial model download

### 1. Clone the repository

```bash
git clone https://github.com/Shrutika1812/AI-Object-Detection.git
cd AI-Object-Detection
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

The webcam window will open and display detected objects with their labels and bounding boxes. Press **`q`** to exit.

## How It Works

1. Loads the pretrained YOLO model.
2. Captures frames from the webcam using OpenCV.
3. Processes each frame to detect objects.
4. Draws bounding boxes and class labels around detected objects.
5. Displays the annotated frames in a live window.

## Future Improvements

- Support image and video file input.
- Display detection confidence scores.
- Track objects across video frames.
- Measure detection performance under different conditions.

## Author

**Shrutika Patil**

[GitHub Profile](https://github.com/Shrutika1812)

---

*Built to gain practical experience with AI-powered computer vision and real-time object detection.*
