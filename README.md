<img src="./images/kuleuven.png" alt="logo1" width="100" style="vertical-align:middle;" /> <img src="./images/logo-black.png" alt="logo2" width="80" style="vertical-align:middle;" />

# OWR-IMU-Dataset 
This repository provides an indoor Optical Wireless Ranging (OWR) + Inertial Measurement Unit (IMU) fusion positioning dataset comprising over **110 K** continuous samples collected over more than **80 minutes**. The data acquisition rates are:

- **RSS measurements**: 27 Hz  
- **IMU readings**: 200 Hz  
- **Ground truth (position & attitude)**: 160 Hz  

# Dramco Setup

<p align="center">
  <img src="./images/Dramco_setup.gif" alt="Animation Demo" width="200">
</p>

The vehicle traverses the floor while on-board sensors capture RSS values from ceiling-mounted infrared LEDs.

## Ceiling View

<p align="center">
  <img src="./images/ceiling.jpg" alt="Ceiling View" width="200">
</p>

The ceiling is equipped with four infrared LEDs, each modulated at a unique frequency for optical ranging calibration.


## Setup Sketch

<p align="center">
  <img src="./images/setup_sketch.jpg" alt="Setup Sketch" width="200">
</p>

Schematic annotation includes LED mounting positions

---

# Datasets Details
**Table 1. Platform Setup Parameters**

<p align="center">
  <img src="./images/table1.png" alt="Platform Setup Parameters" width="400">
</p>

**Table 2. Recorded Dataset Formats**
<p align="center">
  <img src="./images/table2.png" alt="Recorded Dataset Formats" width="400">
</p>