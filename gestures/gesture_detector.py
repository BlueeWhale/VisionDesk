class GestureDetector:

    def __init__(self):

        self.tip_ids = [4, 8, 12, 16, 20]

    def count_fingers(self, landmarks):

        fingers = []

        # Thumb
        if landmarks[self.tip_ids[0]][1] > landmarks[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other Fingers
        for id in range(1, 5):

            if landmarks[self.tip_ids[id]][2] < landmarks[self.tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers.count(1)