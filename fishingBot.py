import cv2
import pyautogui
import time


def is_image_within_image(small_image, big_image_path):
   # Loading images from provided path
   big_image = cv2.imread(big_image_path, cv2.IMREAD_GRAYSCALE)
   
   # Attempting to find small image withing big image
   result = cv2.matchTemplate(big_image, small_image, cv2.TM_CCOEFF_NORMED)
   
   # Define matching threshold - change this number according to your needs, lower it for program to recognise better ath the cost of greater number of mistakes
   threshold = 0.7
   
   # Check if match is above the threshold
   return cv2.minMaxLoc(result)[1] >= threshold


def take_screenshot_and_save():
   # Take screenshot of the current screen
   screenshot = pyautogui.screenshot()
    
   # Save screenshot as currentScreen.png
   screenshot.save("currentScreen.png")


def main():
   small_image = cv2.imread("bobberSplashes.png", cv2.IMREAD_GRAYSCALE)
   
   while True:
      take_screenshot_and_save()
      big_image_path = "currentScreen.png"
      fish_found = is_image_within_image(small_image, big_image_path)

      if fish_found:
         print("Found a fish!")
         pyautogui.rightClick()
         time.sleep(0.2)
         pyautogui.rightClick()
      else:
         print("No fishes around.")
      
      # Define sleep_time - how much will program wait before checking again, change this number if needed - lower to increase accuracy at the cost of performance
      sleep_time = 0.35
      time.sleep(sleep_time)


if __name__ == "__main__":
   main()
