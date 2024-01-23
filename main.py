import os
import numpy as np
import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform


def main():
    # Hardcoded settings
    model_name = "medium"  # Options: "tiny", "base", "small", "medium", "large"
    non_english = False
    energy_threshold = 1000
    record_timeout = 2.0
    phrase_timeout = 3.0
    default_microphone = 'pulse' if 'linux' in platform else None  # Default for Linux. Set to None or specific name for other OS

    phrase_time = None
    data_queue = Queue()
    recorder = sr.Recognizer()
    recorder.energy_threshold = energy_threshold
    recorder.dynamic_energy_threshold = False

    # Setting up the microphone source
    if 'linux' in platform and default_microphone:
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            if default_microphone in name:
                source = sr.Microphone(sample_rate=16000, device_index=index)
                break
    else:
        source = sr.Microphone(sample_rate=16000)

    # Load / Download model
    model = model_name + ".en" if model_name != "large" and not non_english else model_name
    audio_model = whisper.load_model(model)

    transcription = ['']

    with source:
        recorder.adjust_for_ambient_noise(source)

    def record_callback(_, audio: sr.AudioData) -> None:
        data = audio.get_raw_data()
        data_queue.put(data)

    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)
    print("Model loaded.\n")

    while True:
        try:
            now = datetime.utcnow()
            if not data_queue.empty():
                phrase_complete = False
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    phrase_complete = True
                phrase_time = now

                audio_data = b''.join(data_queue.queue)
                data_queue.queue.clear()

                audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
                result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
                text = result['text'].strip()

                if phrase_complete:
                    transcription.append(text)
                else:
                    transcription[-1] = text

                os.system('cls' if os.name == 'nt' else 'clear')
                for line in transcription:
                    print(line)
                print('', end='', flush=True)

                sleep(0.25)
        except KeyboardInterrupt:
            break

    print("\n\nTranscription:")
    for line in transcription:
        print(line)


if __name__ == "__main__":
    main()
