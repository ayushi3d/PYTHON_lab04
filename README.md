# PYTHON_lab04
#Ayushi Srivastava,2502190039




A Python-based fire-fighting robot system that analyzes temperature, smoke, flame, and distance sensor data. Using NumPy, Pandas, SciPy, and Matplotlib, it calculates fire risk, performs statistical analysis, visualizes sensor trends, and determines robot actions such as searching, approaching, or extinguishing fire.
# 🔥 Fire-Fighting Robot Sensor Analysis & Decision System

A robotics-based fire detection and decision-making system that analyzes **temperature, smoke, flame, and distance sensor data** to estimate fire risk and determine the appropriate robot action.

The project uses **NumPy, Pandas, SciPy, and Matplotlib** to process sensor data, perform statistical analysis, calculate a weighted fire-risk score, and visualize sensor trends.

## 🚀 Features

* 🌡️ Temperature monitoring
* 💨 Smoke-level analysis
* 🔥 Flame detection
* 📏 Distance-based fire proximity detection
* 📊 Weighted fire-risk calculation
* 🤖 Rule-based robot decision making
* 📈 Sensor and fire-risk visualization
* 📋 Sensor data management using Pandas
* 📐 Statistical analysis using SciPy

## ⚙️ Working Principle

The system receives sensor readings and normalizes them into comparable values. A weighted fire-risk score is then calculated using:

* Temperature — 40%
* Smoke — 30%
* Distance — 20%
* Flame detection — 10%

Based on the calculated risk:

| Fire Risk | Robot Action    |
| --------- | --------------- |
| 0–25%     | Move / Safe     |
| 25–50%    | Search Area     |
| 50–75%    | Approach Fire   |
| 75–100%   | Extinguish Fire |

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* SciPy
* Matplotlib

## 🔮 Future Scope

This project can be extended into a complete autonomous fire-fighting robot by integrating:

* ROS 2
* Real-time sensors
* Motor controllers
* Autonomous navigation
* Water pump/servo control
* Computer vision
* Fire detection using machine learning
* Gazebo simulation

## 🎯 Objective

The main objective is to understand how **sensor data can be processed and converted into intelligent robotic decisions**, providing a foundation for developing autonomous fire-detection and fire-fighting robots.
