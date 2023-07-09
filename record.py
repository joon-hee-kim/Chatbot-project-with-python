import pyaudio
import wave
import os
import subprocess

def record_audio(filename, seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = seconds
    WAVE_OUTPUT_FILENAME = filename

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def check_for_recording():
    if os.path.exists("recorded_audio.wav"):
        os.remove("recorded_audio.wav")
    record_audio("recorded_audio.wav", 10)
    print("Recording complete. You can now access the recorded_audio.wav file.")
    task_name = "Play Recorded Audio"
    task_command = f'"{os.getcwd()}\\{os.path.basename(__file__)}" play'
    task_trigger = "daily at 09:00" 
    subprocess.call(f'schtasks /create /tn "{task_name}" /tr "{task_command}" /sc daily /st 09:00', shell=True)

def play_recorded_audio():
    if os.path.exists("recorded_audio.wav"):
        subprocess.call(f'"{os.getcwd()}\\recorded_audio.wav"', shell=True)
    else:
        print("No recorded audio file found.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        play_recorded_audio()
    else:
        check_for_recording()


import os

def play_recorded_audio():
    os.system("start recorded_audio.wav")

play_recorded_audio()
