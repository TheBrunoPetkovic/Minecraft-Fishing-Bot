# Minecraft Fishing Bot

## Overview
This Python script automates fishing in Minecraft using image recognition and mouse automation. By analyzing screenshots of the game, the script detects the appearance of the fishing bobber and automatically performs the fishing action.

## Features
- **Image Recognition**: Utilizes OpenCV to perform template matching for detecting the fishing bobber splash.
- **Mouse Automation**: Utilizes PyAutoGUI to simulate mouse clicks for fishing.
- **Adjustable Parameters**: Thresholds and sleep times can be adjusted to customize the bot's performance.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- PyAutoGUI
- Minecraft Java Edition (PC)

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install required Python packages using pip:
```
pip install opencv-python pyautogui
```
3. Clone this repository to your local machine:
```
git clone https://github.com/TheBrunoPetkovic/Minecraft-Fishing-Bot.git
```

## Usage
1. Run the `fishingBot.py` script.
2. Launch Minecraft Java Edition and position the fishing rod in the desired location.
3. The bot will automatically detect and click on the fishing bobber when it appears.

## Configuration
- **Threshold**: Adjust the matching threshold in the `is_image_within_image` function to fine-tune detection accuracy.
- **Sleep Time**: Adjust the sleep time in the `main` function to control the frequency of detection checks.

## Disclaimer
This script is intended for educational purposes only. Usage of automated scripts in multiplayer environments may violate the terms of service of the game. Use at your own risk.

## Notes
Minecraft must be in windowed mode at maximum window size
