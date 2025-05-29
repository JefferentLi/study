import numpy as np
import soundfile as sf
import pyaudio

# PCM参数
pcm_path = 'short_music1.pcm'
wav_path = 'music1.wav'
channels = 1    # 单声道
samplerate = 8000  # 采样率
samplewidth = 2  # 每个采样点字节数，16位PCM为2字节

# 1. 读取PCM并保存为WAV
with open(pcm_path, 'rb') as pcmfile:
    pcm_data = pcmfile.read()
audio = np.frombuffer(pcm_data, dtype=np.int16)  # 16位
sf.write(wav_path, audio, samplerate, subtype='PCM_16')

# 2. 读取WAV信息
info = sf.info(wav_path)
print("音频信息:", info)

# 3. 播放音频
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16, channels=channels, rate=samplerate, output=True)
stream.write(audio.tobytes())
stream.stop_stream()
stream.close()
pa.terminate()