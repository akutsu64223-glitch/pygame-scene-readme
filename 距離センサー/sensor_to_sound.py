import argparse
import time

import pygame
import serial

from distance_mapping import distance_to_frequency
from play_frequency import generate_sine_wave

SAMPLE_RATE = 44100


def main():
    parser = argparse.ArgumentParser(description="距離センサーの値を音に変換する")
    parser.add_argument("port", help="Arduinoが接続されているシリアルポート (例: COM3)")
    parser.add_argument(
        "--baud", type=int, default=9600,
        help="ボーレート。Arduinoスケッチ側のSerial.begin()と揃える(デフォルト: 9600)"
    )
    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    time.sleep(2) 
    ser.reset_input_buffer()  

    pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=2)

    print("読み取り開始。Ctrl+Cで終了します。")
    try:
        while True:
            if ser.in_waiting > 0:
                chunk = ser.read(ser.in_waiting).decode("utf-8", errors="ignore")
                lines = [l for l in chunk.splitlines() if l.strip()]
                if not lines:
                    continue
                line = lines[-1]
            else:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if not line:
                    continue

            try:
                distance_cm = float(line)
            except ValueError:
                continue

            freq = distance_to_frequency(distance_cm)
            print(f"距離: {distance_cm:6.1f} cm -> {freq:7.1f} Hz")

            wave = generate_sine_wave(freq, duration=0.15)
            sound = pygame.sndarray.make_sound(wave)
            sound.play()
    except KeyboardInterrupt:
        print("終了します")
    finally:
        ser.close()


if __name__ == "__main__":
    main()