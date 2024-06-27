import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    frame_height, frame_width, success = img.shape
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    outpt = mp_hands.process(rgb_img)
    hand = outpt.multi_hand_landmarks
    if hand:
        for hands in hand:
            drawing_utils.draw_landmarks(img, hands)
            landmarks = hands.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=img, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=img, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
        cv2.line(img, (x1, y1), (x2, y2), (128, 0, 128), 5)
        if dist > 20:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Image", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()