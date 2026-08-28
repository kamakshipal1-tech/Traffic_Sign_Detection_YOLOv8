# 🚦 Traffic Sign Detection using YOLOv8

## 📌 Project Overview

Traffic signs play a crucial role in ensuring road safety by providing drivers with important instructions, warnings, and regulations. Manual monitoring of traffic signs is time-consuming and not scalable, making automated detection systems an essential component of modern Intelligent Transportation Systems (ITS), Advanced Driver Assistance Systems (ADAS), and autonomous vehicles.

This project presents an end-to-end deep learning solution for Traffic Sign Detection using the YOLOv8 object detection model. The model is trained to identify multiple categories of traffic signs from road images and accurately localize them using bounding boxes. A user-friendly Streamlit web application is also developed to allow users to upload road images and visualize detection results in real time.

---

# 🎯 Business Problem

Road accidents frequently occur due to missed or incorrectly interpreted traffic signs. Human drivers may overlook important signs because of poor visibility, weather conditions, fatigue, or distractions.

An automated traffic sign detection system can:

- Improve road safety
- Assist autonomous driving systems
- Support Advanced Driver Assistance Systems (ADAS)
- Enable intelligent traffic monitoring
- Reduce human error during driving

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Detect traffic signs from road images.
- Classify detected traffic signs into their respective categories.
- Draw accurate bounding boxes around detected signs.
- Display prediction confidence for each detection.
- Develop an interactive Streamlit web application for real-time image inference.
- Deploy the project for public use.

---

# 🧠 Deep Learning Approach

This project uses **YOLOv8 (You Only Look Once Version 8)**, one of the latest state-of-the-art object detection architectures developed by Ultralytics.

Unlike traditional object detection methods that perform region proposal and classification separately, YOLO performs object localization and classification simultaneously in a single forward pass, making it significantly faster while maintaining high accuracy.

---

# 🗂️ Dataset

The dataset contains images of road scenes with annotated traffic signs belonging to multiple categories.

Each image includes:

- Traffic sign objects
- Bounding box coordinates
- Class labels

The dataset is organized in YOLO format:

```
train/
    images/
    labels/

valid/
    images/
    labels/

test/
    images/
    labels/

data.yaml
```

---

# 🛠️ Project Workflow

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
YOLOv8 Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Traffic Sign Prediction
        │
        ▼
Streamlit Deployment
```

---

# ⚙️ Technologies Used

- Python
- YOLOv8
- Ultralytics
- OpenCV
- NumPy
- Pillow
- Streamlit
- Google Colab
- Git
- GitHub

---

# 📊 Model Training

The model was fine-tuned using a pre-trained YOLOv8 model.

Training configuration:

| Parameter | Value |
|------------|--------|
| Model | YOLOv8 Nano |
| Epochs | 50 |
| Image Size | 640 × 640 |
| Batch Size | 16 |
| Optimizer | Default YOLO Optimizer |
| Framework | Ultralytics |

---

# 📈 Evaluation Metrics

The model performance is evaluated using:

- Precision
- Recall
- mAP@50
- mAP@50-95
- Confusion Matrix
- Precision-Recall Curve

These metrics provide a comprehensive understanding of both localization and classification performance.

---

# 🚀 Streamlit Web Application

A web application has been developed using Streamlit that enables users to perform traffic sign detection without requiring any programming knowledge.

App Link: https://trafficsigndetectionyolov8-mgts9mhrnuhtysyfwnx6qp.streamlit.app/

### Features

- Upload road images
- Detect traffic signs
- Draw bounding boxes
- Display confidence scores
- Interactive and responsive interface
- Fast inference using YOLOv8

---

# 📁 Project Structure

```
Traffic_Sign_Detection_YOLOv8
│
├── app.py
├── best.pt
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Traffic_Sign_Detection_YOLOv8.git
```

Move into the project directory

```bash
cd Traffic_Sign_Detection_YOLOv8
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```


# 💡 Key Learnings

Through this project, I gained practical experience in:

- Object Detection using YOLOv8
- Transfer Learning
- Bounding Box Prediction
- Computer Vision
- Deep Learning Model Training
- Performance Evaluation
- Streamlit Deployment
- Model Inference
- GitHub Project Deployment

---

# 🔮 Future Improvements

Possible enhancements include:

- Real-time webcam detection
- Video traffic sign detection
- Live traffic surveillance
- Mobile deployment
- ONNX optimization
- TensorRT acceleration
- Multi-language support
- GPS-based traffic sign assistance

---

# 🎯 Real-World Applications

- Autonomous Vehicles
- Advanced Driver Assistance Systems (ADAS)
- Smart Cities
- Intelligent Transportation Systems
- Driver Assistance Applications
- Road Safety Monitoring
- Traffic Surveillance

---

# 👩‍💻 Author

**Kamakshi Pal**

Applied Mathematics Undergraduate  
Delhi Technological University (DTU)

GitHub: https://github.com/kamakshipal1-tech

---

# ⭐ Acknowledgements

- Ultralytics YOLOv8
- Streamlit
- OpenCV
- Roboflow
- Kaggle
- Google Colab

---

If you found this project useful, consider giving it a ⭐ on GitHub.
