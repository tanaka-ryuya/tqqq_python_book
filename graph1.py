import matplotlib.pyplot as plt
import yfinance as yf
from font import set_japanese_font

# 日本語フォント設定
set_japanese_font()

# SPYのデータ取得（調整後Closeはデフォルト）
spy = yf.download("SPY", start="2000-01-01", end="2025-06-15")

# 月次に変換（'M' → 'ME'）
spy_monthly = spy['Close'].resample('ME').last()
cumulative_return = (spy_monthly / spy_monthly.iloc[0]) * 100

# グラフ描画（モノクロ対応）
plt.figure(figsize=(12, 6))
plt.plot(
    cumulative_return.index,
    cumulative_return,
    color='black',
    linestyle='solid',
    linewidth=2,
    label="S&P500（SPY）"
)
plt.title("グラフ1：S&P500累積リターン（2000〜2025、月次）", fontsize=14)
plt.xlabel("日付", fontsize=12)
plt.ylabel("累積リターン（初期値＝100）", fontsize=12)
plt.grid(True, linestyle='dotted')
plt.legend(loc='upper left', fontsize=11)
plt.tight_layout()
plt.show()







