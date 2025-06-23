# 🧫 Cell Automation with Opentrons OT-2

Welcome to my OT-2 learning and automation hub!  
This repository contains a growing collection of protocols, tools, and functions designed to automate **cell culturing workflows** using the [Opentrons OT-2](https://opentrons.com/ot-2) robot and Python API.

---

## 📌 Goals & Focus

Over the past few months, I’ve been exploring:
- 🔬 Custom pipetting protocols for **cell culturing** (e.g. passaging, media exchange)
- 🧪 **Residual volume minimization** techniques for improved consistency
- 🛠️ Development of custom **labware definitions** and flexible helper functions
- 🔍 Protocol simulation with **visual summaries** and **color-coded console output**

---

## 📁 What’s Inside

### 🧠 Core Components

| Folder/File | Description |
|-------------|-------------|
| `protocols/` | Experimental and working protocols for automation tasks |
| `validation/` | Scripts for testing tip height, volume accuracy, and well offsets |
| `labware/` | Custom JSON labware definitions built from real plate offsets, and scripts to make them |
| `simulation/` | Enhanced `opentrons_simulate.py` for readable outputs |
| `utils/` | Helper functions to improve pipetting (aspirate, distribute, etc.) |
| `README.md` | You are here — repo overview and documentation |

---

## ⚗️ Validation Methods

The `validation/` folder includes techniques we’ve used to:
- 🧮 Test various plates and wells for residual volume amounts **weighted z-height averaging**
- 📏 Determine **standard curve** to measure amounts of liquid and compare trends
- 🧰 Trying different methods of bubble removal and other methods when aspirating fluid

Example scripts:
- `ResidueTesting.py`
- `StandardCurve.py`
- `TitltedTouchTipTest.py`

These experiments were key to minimizing inconsistency caused by plate tilt and deck offsets.

---

## 🖼️ Custom Labware Tools

Working with inconsistent plate heights? The `labware/` folder contains:
- Custom JSON files built using **real well offset data**
- Scripts to autogenerate definitions based on physical z-height changes
- Adaptable tools for converting average well coordinates into usable Opentrons labware

Each JSON is readable, editable, and ready to use in Protocol Designer or Python.

---

## 🧠 Simulation & Debugging

Tired of raw simulation outputs?  
Try our enhanced `opentrons_simulate.py` version found in the `simulation/` folder:

Features:
- ✅ Prints **color-coded terminal logs** (pickup, drop, aspirate, dispense, etc.)
- 📋 Summarizes pipetting actions at the end of each protocol
- 🔄 Matches physical action timing to API outputs for more accurate debugging

---

## 🧪 Smart Pipetting Utilities

Explore the `utils/` folder for upgraded functions like:
- `enhanced_distribute()`: just a better version of the distribute function, needs updates

All designed to be plug-and-play with your custom protocols, but may need some tweaking for ordering and amount of plates and etc.

---

## 🧱 File-by-File Docs (Coming Soon)

Each major folder will soon include a `README.md` that documents:
- What the scripts do
- How they were validated
- How to run them + dependencies
- Troubleshooting tips
