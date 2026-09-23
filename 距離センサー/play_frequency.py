
import argparse
 
import numpy as np
import pygame
 
 
def generate_sine_wave(frequency=440.0, duration=1.0, sample_rate=44100, amplitude=0.5):
    """指定した周波数のsin波をnumpy配列(ステレオ)として生成する"""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    audio = (wave * 32767).astype(np.int16)
    stereo = np.column_stack([audio, audio])
    return stereo
 
 
def play_tone(frequency=440.0, duration=1.0, sample_rate=44100):
    """指定した周波数・長さで音を鳴らす"""
    pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
    wave = generate_sine_wave(frequency, duration, sample_rate)
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
    pygame.time.wait(int(duration * 1000))
 
 
def main():
    parser = argparse.ArgumentParser(description="指定した周波数のsin波を再生する")
    parser.add_argument("frequency", type=float, help="周波数(Hz) 例: 440")
    parser.add_argument(
        "-d", "--duration", type=float, default=1.0,
        help="再生時間(秒) デフォルト: 1.0"
    )
    args = parser.parse_args()
 
    print(f"{args.frequency}Hz を {args.duration}秒 再生します")
    play_tone(args.frequency, args.duration)
 
 
if __name__ == "__main__":
    main()
 
