# **Football Match Analysis System**

##  **Project Overview**
This project is an **Automated Football Match Analysis System** designed to process and analyze football game footage intelligently. The system leverages advanced **computer vision**, **machine learning**, and **data analysis** techniques to extract meaningful insights from match videos. It can detect and differentiate between players, referees, and goalkeepers, assign team colors dynamically, estimate ball possession, track player speeds, and even account for camera movements.

The project processes match footage frame-by-frame, applies robust object tracking algorithms, and overlays key metrics directly onto the video output for easy visualization.

---

##  **Key Features**

### 1. **Player, Referee, and Ball Detection **
- Detects players, referees, and the ball using the **YOLO model**.
- Differentiates goalkeepers from regular players by modifying class IDs.
- Tracks player and ball positions frame-by-frame.
- Handles missing object positions through interpolation.
- Annotates bounding boxes and IDs for every tracked object.

### 2. **Team Differentiation **
- Differentiates teams based on jersey colors using **K-Means clustering**.
- Dynamically assigns team IDs and colors.
- Applies jersey color analysis on the upper half of detected player bounding boxes to minimize errors.
- Clusters detected colors and assigns them to teams.

### 3. **Ball Possession Tracking **
- Identifies the closest player to the ball using **bounding box distances**.
- Tracks ball possession across frames.
- Handles edge cases where no player is close enough to claim possession.

### 4. **Camera Movement Estimation **
- Tracks camera panning and movement using **Optical Flow (Lucas-Kanade Method)**.
- Adjusts player and object positions to account for camera movements.
- Provides detailed movement overlays on video frames.

### 5. **Player Speed and Distance Calculation **
- Calculates player speed (in km/h) and distance covered (in meters).
- Handles position changes across multiple frames.
- Annotates speed and distance metrics directly on video frames.

### 6. **Video Output with Overlays **
- Integrates all functionalities into a seamless pipeline.
- Processes video footage and saves an annotated version.
- Overlays:
   - Player IDs and team colors.
   - Ball possession data.
   - Camera movement indicators.
   - Player speeds and distances.

---

## **Setup & Installation**

Make sure you have **Python 3.10** installed.

1. **Clone the repository:**
   ```bash
   git clone <repo-link>
   cd <project-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare YOLO Model:**
   - Place your YOLO model (`best.pt`) in the `models` folder.

4. **Video Input:**
   - Place your input video in the `Data/` folder.

---

## **How to Run the Project**

Run the main script to process the video:
```bash
python main.py
```

- Input video should be located in the `Data/` directory.
- Processed and annotated video will be saved in `output_videos/`.

---

## **Dependencies**

Dependencies are listed in `requirements.txt`:
```
ultralytics
roboflow
opencv-python
supervision
scikit-learn
```

---

## **Technologies Used**

- **YOLO (Ultralytics):** Real-time object detection.
- **OpenCV:** Video and image processing.
- **Supervision:** Object tracking.
- **Scikit-learn:** K-Means clustering for team assignment.
- **Numpy & Pandas:** Data processing and interpolation.

---

## **Contribution Guidelines**

1. **Fork the repository.**
2. Create a feature branch:
   ```bash
   git checkout -b feature-your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-your-feature
   ```
5. Open a Pull Request.

---
---

This system brings football analysis to a whole new level, blending advanced technologies to provide precise and insightful results. Enjoy building and analyzing!

