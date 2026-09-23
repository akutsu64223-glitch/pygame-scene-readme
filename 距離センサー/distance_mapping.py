def distance_to_frequency(
    distance_cm,
    dist_min=5.0,
    dist_max=100.0,
    freq_min=200.0,
    freq_max=2000.0,
    invert=True,
):
    """距離(cm)を周波数(Hz)に変換する
 
    invert=True  : 距離が近いほど周波数が高い(デフォルト)
    invert=False : 距離が遠いほど周波数が高い
    """
    # 範囲外の値(センサーノイズや異常値)をクランプして計算を安定させる
    d = max(dist_min, min(dist_max, distance_cm))
 
    # 距離を 0.0(dist_min側)〜1.0(dist_max側) に正規化
    ratio = (d - dist_min) / (dist_max - dist_min)
 
    if invert:
        ratio = 1.0 - ratio  # 近い(dist_min側)ほど1.0に近づく=周波数が高くなる
 
    # 指数マッピング: f = f_min * (f_max/f_min)^ratio
    frequency = freq_min * (freq_max / freq_min) ** ratio
    return frequency
 
 
if __name__ == "__main__":
    # 動作確認: 距離をいくつか試して周波数の対応を見る
    test_distances = [5, 15, 30, 50, 70, 100]
    print("距離(cm) -> 周波数(Hz)")
    for d in test_distances:
        f = distance_to_frequency(d)
        print(f"  {d:>3} cm -> {f:>7.1f} Hz")
