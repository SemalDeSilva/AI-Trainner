# AI Trainer: Pose Estimation and Repetition Counter

This project is an AI-based workout trainer that uses **OpenCV** and **MediaPipe** to track a user's pose and count repetitions during exercises like dumbbell curls. It leverages pose detection to estimate the angles between body joints and calculate exercise reps based on these angles.


## Introduction

The **AI Trainer** is designed to track the user's body movements in real-time and count exercise repetitions using pose estimation techniques. It can analyze video input and provide visual feedback on how well the user performs a particular exercise, such as dumbbell curls. This project demonstrates pose detection, angle calculation, and repetition counting by processing videos using OpenCV and MediaPipe.

## Features

- Real-time pose detection using **MediaPipe Pose**.
- Calculation of angles between key joints.
- Visual feedback with real-time angle display.
- Automatic repetition counter for exercises like curls.
- FPS (frames per second) display for performance monitoring.
- Customizable to track different body movements and exercises.
- Works with both pre-recorded videos and webcam input.

## Libraries Used

This project uses the following Python libraries:

- **OpenCV**: For video processing and real-time display.
- **MediaPipe**: For detecting body landmarks and pose estimation.
- **NumPy**: For interpolation and mathematical operations.
- **Time**: For tracking performance and calculating FPS.

## How It Works

1. **Pose Detection**: 
   - The `PoseModule.py` uses **MediaPipe** to detect and track 33 body landmarks from video frames. 
   - The pose landmarks are identified with specific IDs to locate body parts such as shoulders, elbows, and wrists.

2. **Angle Calculation**: 
   - The angle between key joints (e.g., elbow and shoulder) is calculated using trigonometric functions. This angle helps determine the stage of the exercise (e.g., up or down).

3. **Repetition Counting**: 
   - Based on the calculated angle, the code detects whether the exercise is in the “up” or “down” phase and increments the rep count accordingly.
   - A progress bar and percentage display are provided to visually track each repetition.

4. **Performance Monitoring**: 
   - The FPS (frames per second) is calculated and displayed to monitor the performance of the system.

## Installation

To set up this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/AITrainer.git
