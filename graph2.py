from font import set_japanese_font
set_japanese_font()

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 実データ取得（SPY、調整済み価格）
spy = yf.download("SPY", start="2020-01-01", end="2022-01-01", auto_adjust=True)
price_series = spy['Close']

# 月初を抽出（積立用）
monthly_dates = price_series.resample('MS').first().index
monthly_invest = 10000
total_investment = monthly_invest * len(monthly_dates)

# 積立投資（毎月1万円）
shares_dca = pd.Series(0.0, index=price_series.index)
shares_total = 0
for date in monthly_dates:
    if date in price_series:
        shares = monthly_invest / price_series.loc[date]
        shares_total += shares
        shares_dca.loc[date:] = shares_total
value_dca = shares_dca * price_series

# 一括投資：最初の積立日（存在する最初の営業日）を探す
first_valid_date = price_series.index[price_series.index >= monthly_dates[0]][0]
initial_price = price_series.loc[first_valid_date]
shares_lump = total_investment / initial_price
value_lump = price_series * shares_lump


# グラフ描画
plt.figure(figsize=(14, 6))

# 上段：SPYチャート
plt.subplot(2, 1, 1)
plt.plot(price_series.index, price_series, color='gray', linewidth=1.5)
plt.title("SPY実チャート（2020〜2021年）", fontsize=13)
plt.ylabel("調整済み終値（USD）", fontsize=11)
plt.grid(True, linestyle='dotted')

# 下段：積立 vs 一括
plt.subplot(2, 1, 2)
plt.plot(price_series.index, value_lump, label='一括投資（36万円）', color='black', linestyle='solid', linewidth=2)
plt.plot(price_series.index, value_dca, label='積立投資（月1万円×24回）', color='black', linestyle='dashed', linewidth=2)
plt.title("積立 vs 一括：SPY実データ比較（2020〜2021年）", fontsize=13)
plt.xlabel("日付", fontsize=11)
plt.ylabel("資産評価額（円換算）", fontsize=11)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='dotted')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])  # マージン付きtight_layout
plt.show()