# a.txtを読み込む
with open("a.txt", "r", encoding='UTF-8') as f:
    # ファイルの内容を1行ずつ取得
    lines = f.readlines()
    # ファイルの内容を1行ずつ表示
    for line in lines:
        print(line)

# b.txtを書き込みモードで開く
with open('b.txt', 'w', encoding='UTF-8') as f:
    # ファイルの内容を1行ずつ書き込む
    for line in reversed(lines):
        # 文字を反転する
        converted_line=line[::-1]
        # ファイルに書き込む
        f.write(converted_line)
