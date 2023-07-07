import argparse

# コマンドライン引数のパーサーを作成
parser = argparse.ArgumentParser()
parser.add_argument('-a', type=int, help='数値を指定してください')
parser.add_argument('-b', type=int, help='数値を指定してください')

# 引数をパース
args = parser.parse_args()

# 掛け算の結果を計算
result = args.a * args.b

# 結果を表示
print(f'結果: {result}')
