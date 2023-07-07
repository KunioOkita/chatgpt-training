import argparse
import csv
import statistics

# コマンドライン引数のパーサーを作成
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help='ファイルパスを指定してください')

# 引数をパース
args = parser.parse_args()

# ファイルパスを取得
file_path = args.f

# ファイルを開いてCSVデータを読み込む
try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        cpu_values = [float(row[1]) for row in reader]  # CPU使用率の値を抽出
except FileNotFoundError:
    print("ファイルが見つかりません。")
    exit(1)
except IndexError:
    print("CSVフォーマットが正しくありません。")
    exit(1)
except ValueError:
    print("CPU使用率が数値ではありません。")
    exit(1)

# CPU使用率の統計情報を計算
mean_value = statistics.mean(cpu_values)
median_value = statistics.median(cpu_values)
stdev_value = statistics.stdev(cpu_values)

# 結果をMarkdown表形式で表示
print("| 統計情報 | 値 |")
print("|---|---|")
print(f"| 平均値 | {mean_value:.2f} |")
print(f"| 中央値 | {median_value:.2f} |")
print(f"| 標準偏差 | {stdev_value:.2f} |")
