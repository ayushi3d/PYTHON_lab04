# ayushi 

#🏭 Automated Manufacturing Inspection & Tool-Wear Detection System

A Python-based automated manufacturing inspection system that simulates a quality-control station inspecting **200 manufactured parts** based on their diameter tolerance. The system automatically generates realistic dimensional variations, classifies each part as accepted or rejected, monitors rejection patterns, detects possible **tool wear**, and generates a final stamped shift report.

## 🚀 Features

* 🏭 Automated inspection of 200 parts
* 📏 Diameter tolerance checking
* ✅ Automatic accept/reject classification
* ❌ Rejected-part tracking
* 🔢 Consecutive-reject monitoring
* 🔧 Tool-wear simulation using dimensional drift
* ⚠️ Automatic tool-wear alarm detection
* 📊 Acceptance percentage calculation
* 🕐 Timestamped shift report
* 📋 First-alarm and total-alarm tracking
* 📐 Nominal area calculation

## ⚙️ Working Principle

The system generates random diameter values to simulate natural manufacturing variation. Each part is inspected automatically and compared with the defined tolerance limits.

**Tolerance Range:**

`24.90 mm – 25.10 mm`

Parts within this range are classified as **ACCEPTED**, while parts outside the range are classified as **REJECTED**.

The program also maintains a counter for consecutive rejected parts. The counter resets whenever an accepted part is detected. If **three consecutive parts are rejected**, the system generates a tool-wear alarm.

After **part 100**, the random diameter range is shifted upward by **0.05 mm** to simulate a worn cutting tool producing increasingly oversized parts. This dimensional drift increases the probability of rejection and allows the alarm system to identify the possible tool-wear condition.

### 🔧 Tool-Wear Detection Logic

| Condition               | System Response        |
| ----------------------- | ---------------------- |
| Part within tolerance   | Accept                 |
| Part outside tolerance  | Reject                 |
| 1–2 consecutive rejects | Continue monitoring    |
| 3 consecutive rejects   | ⚠️ Tool Wear Suspected |

## 📊 Shift Report

After all 200 parts have been inspected, the program generates a stamped shift report containing:

* Operator names
* Total number of inspected parts
* Total accepted parts
* Total rejected parts
* Acceptance percentage
* Tolerance band used
* Number of tool-wear alarms
* Part number of the first alarm
* Nominal area of the part
* Date and time of the inspection

## 🛠️ Technologies Used

* Python
* Random
* DateTime
* Math
* For Loops
* Conditional Statements
* Variables and Counters

## 🔮 Future Scope

This simulation can be developed into a real-world **smart manufacturing quality-control system** by integrating:

* Industrial measurement sensors
* Arduino / ESP32
* PLC-based control
* Computer vision
* Machine-learning-based defect detection
* IoT-based production monitoring
* ROS 2
* Digital twin simulation
* Real-time manufacturing dashboards

## 🎯 Objective

The main objective of this project is to understand how Python can be used to automate a manufacturing inspection process, monitor product quality, identify possible tool wear through rejection patterns, and generate meaningful production statistics. The project demonstrates the practical use of loops, conditional logic, counters, random data generation, fault detection, and automated reporting in a manufacturing environment.
