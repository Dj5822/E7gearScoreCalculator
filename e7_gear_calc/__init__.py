from PIL import Image
import pyautogui
import pytesseract
import cv2
import numpy as np

def get_rows(str):
    rows = str.split('\n')
    rows.pop()
    return rows

def get_info(row):
    return [''.join([i for i in row if not i.isdigit() and i != " "]), ''.join([i for i in row if i.isdigit()])]

def get_gear_score_from_image(image):
    multipliers = {
        "Attack%": 1,
        "Health%": 1,
        "EffectResistance%": 1,
        "Effectiveness%": 1,
        "Attack": (1/12),
        "Health": (1/60),
        "Defense": (1/6),
        "CriticalHitChance%": 1.6,
        "CriticalHitDamage%": 1.1,
        "Speed": 1.8
    }

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    gearImage = np.array(image)

    hsv = cv2.cvtColor(gearImage, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 80])
    upper = np.array([0, 0, 255])

    filteredImg = cv2.inRange(hsv, lower, upper)

    result = pytesseract.image_to_string(filteredImg)
    
    rows = get_rows(result)
    score = 0

    for row in rows:
        stat_name, statValue = get_info(row)
        print(stat_name + ": " + statValue)
        score += multipliers[stat_name] * int(statValue)
    
    return score

def main():
    mainImage = pyautogui.screenshot(region=(693, 223, 520, 770))
    statsImage = pyautogui.screenshot(region=(693, 773, 500, 200))
    print("Score: " + str(get_gear_score_from_image(statsImage)))
    mainImage.show()

main()
