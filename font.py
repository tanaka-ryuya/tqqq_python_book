
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

def set_japanese_font():
    """
    環境ごとに日本語対応フォントを設定します。
    Windows・macOS・LinuxでNotoSansJPなどが対象です。
    """
    font_paths = [
        "C:/Windows/Fonts/NotoSansJP-VF.ttf",                        # Windows
        "/System/Library/Fonts/Supplemental/NotoSansJP-Regular.otf",     # macOS
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",        # Ubuntu/Linux
    ]

    for path in font_paths:
        if os.path.exists(path):
            font_prop = fm.FontProperties(fname=path)
            plt.rcParams["font.family"] = font_prop.get_name()
            return font_prop

    raise FileNotFoundError("日本語フォントが見つかりません。NotoSansJPをインストールしてください。")
