import cv2
import time
import webbrowser
import pywhatkit
from voice.clap_detector import detect_clap
from gestures.hand_tracking import HandTracker
from gestures.gesture_detector import GestureDetector

from voice.speech_control import listen, speak

from automation.app_launcher import (
    open_youtube,
    open_instagram,
    open_telegram,
    open_google,
    open_spotify,
    open_chatgpt,
    open_calculator,
    open_notepad
)

# Camera
cap = cv2.VideoCapture(0)

# Objects
tracker = HandTracker()
detector = GestureDetector()

# Delay System
last_action_time = 0
cooldown = 3

while True:

    success, img = cap.read()

    img = cv2.flip(img, 1)

    # Detect Hands
    img = tracker.detect_hands(img)

    # Get Landmarks
    landmarks = tracker.get_landmarks(img)

    if len(landmarks) != 0:

        fingers = detector.count_fingers(landmarks)

        gesture = ""

        current_time = time.time()

        # Gesture Logic
        if fingers == 1:

            gesture = "Opening YouTube"

            if current_time - last_action_time > cooldown:
                open_youtube()
                last_action_time = current_time

        elif fingers == 2:

            gesture = "Opening Telegram"

            if current_time - last_action_time > cooldown:
                open_telegram()
                last_action_time = current_time

        elif fingers == 3:

            gesture = "Opening Instagram"

            if current_time - last_action_time > cooldown:
                open_instagram()
                last_action_time = current_time

        elif fingers == 4:

            gesture = "Opening Spotify"

            if current_time - last_action_time > cooldown:
                open_spotify()
                last_action_time = current_time

        elif fingers == 0:

            gesture = "Opening ChatGPT"

            if current_time - last_action_time > cooldown:
                open_chatgpt()
                last_action_time = current_time

        elif fingers == 5:

            gesture = "Opening Google"

            if current_time - last_action_time > cooldown:
                open_google()
                last_action_time = current_time

        # Show Gesture Text
        cv2.putText(
            img,
            gesture,
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 255),
            3
        )

    # Show Window
    cv2.imshow("VisionDesk", img)
    key = cv2.waitKey(1) & 0xFF
        # Press C for Clap Detection
    if key == ord('c'):

        if detect_clap():

            speak("Clap detected")

            open_google()
        else:
        # Detect Hands Normally
            img = tracker.detect_hands(img)

        landmarks = tracker.get_landmarks(img)

    # Keyboard Controls
    # Press V for Voice Assistant
    if key == ord('v'):

        speak("Voice mode activated")

        command = listen()

        # YouTube
        if "youtube" in command:

            speak("Opening YouTube")
            open_youtube()

        # Telegram
        elif "telegram" in command:

            speak("Opening Telegram")
            open_telegram()

        # Instagram
        elif "instagram" in command:

            speak("Opening Instagram")
            open_instagram()

        # Spotify
        elif "spotify" in command:

            speak("Opening Spotify")
            open_spotify()

        # ChatGPT
        elif "chatgpt" in command:

            speak("Opening ChatGPT")
            open_chatgpt()

        # Calculator
        elif "calculator" in command:

            speak("Opening Calculator")
            open_calculator()

        # Notepad
        elif "notepad" in command:

            speak("Opening Notepad")
            open_notepad()

        # Google Search
        elif "search" in command:

            speak("What should I search?")

            search_query = listen()

            speak(f"Searching for {search_query}")

            webbrowser.open(
                f"https://www.google.com/search?q={search_query}"
            )
        

        # Play Music on YouTube
        elif "play" in command:

            song = command.replace("play", "")

            speak(f"Playing {song} on YouTube")

            pywhatkit.playonyt(song)

        # Unknown Command
        else:

            speak("Command not recognized")

    # Press Q to Exit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()