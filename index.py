import os

def txt_to_lrc(txt_file, interval_ms=500):
    """
    把 TXT 转换成 LRC
    :param txt_file: 输入的 TXT 文件路径
    :param interval_ms: 每行间隔的毫秒数，默认 500 毫秒
    """
    if not os.path.isfile(txt_file):
        print("文件不存在:", txt_file)
        return

    # 输出文件路径
    base, _ = os.path.splitext(txt_file)
    lrc_file = base + ".lrc"

    with open(txt_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    with open(lrc_file, "w", encoding="utf-8") as f:
        total_ms = 0
        for line in lines:
            minutes = (total_ms // 1000) // 60
            seconds = (total_ms // 1000) % 60
            centiseconds = (total_ms % 1000) // 10  # 转成两位数，LRC通常到百分之一秒
            timestamp = f"[{minutes:02d}:{seconds:02d}.{centiseconds:02d}]"
            f.write(f"{timestamp}{line}\n")
            total_ms += interval_ms

    print(f"已生成: {lrc_file}")


if __name__ == "__main__":
    txt_path = input("请输入txt文件路径: ").strip('"').strip("'")
    try:
        interval_ms = int(input("请输入每行间隔的毫秒数 (默认500): ") or "500")
    except ValueError:
        interval_ms = 500

    txt_to_lrc(txt_path, interval_ms)
