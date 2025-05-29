# 参数设置
pcm_path = 'music1.pcm'
out_pcm_path = 'short_music1.pcm'
sample_rate = 8000      # 采样率
channels = 1             # 声道数
sample_width = 2         # 每采样字节数（16位=2字节）
target_duration_sec = 10 # 目标时长（秒）

# 计算每秒字节数和目标总字节数
bytes_per_sec = sample_rate * channels * sample_width
target_bytes = bytes_per_sec * target_duration_sec

# 读取并截取
with open(pcm_path, 'rb') as f_in:
    pcm_data = f_in.read(target_bytes)

with open(out_pcm_path, 'wb') as f_out:
    f_out.write(pcm_data)

print(f"已生成 {target_duration_sec} 秒的PCM文件：{out_pcm_path}")