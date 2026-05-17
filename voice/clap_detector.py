import sounddevice as sd
import numpy as np

def detect_clap(threshold=0.7):

    duration = 1  # seconds

    sample_rate = 44100

    print("Listening for clap...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    volume = np.linalg.norm(recording)

    print("Volume:", volume)

    if volume > threshold:

        return True

    return False