import cv2
import mediapipe as mp

class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils

    def detect_hands(self, img, draw=True):

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                if draw:

                    self.mpDraw.draw_landmarks(
                        img,
                        handLms,
                        self.mpHands.HAND_CONNECTIONS
                    )

        return img

    def get_landmarks(self, img):

        landmark_list = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(hand.landmark):

                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)

                landmark_list.append([id, cx, cy])

        return landmark_list