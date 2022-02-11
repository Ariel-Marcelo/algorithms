import numpy as np
import pyautogui as pg
import cv2


#screenshot = pg.screenshot('screenshot.png')

screenshot = pg.screenshot()

screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

logo = pg.locateOnScreen('logo.png')

# cv2.rectangle (
#     screenshot,
#     {logo.left, logo.top},
#     {logo.left + logo.width, logo.top + logo.height},
#     {0, 255, 255},
#     2
# )

cv2.inshow('screenshot', screenshot)

cv2.waitKey(0)

cv2.destroyAllWindows()