from voice.speech_control import listen, speak

speak("VisionDesk Activated")

command = listen()

print(command)

speak(f"You said {command}")