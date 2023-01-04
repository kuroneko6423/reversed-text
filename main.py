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
        # reversed(line) は、文字列 line を逆順に並び替えたイテレータを返します。
        # ''.join(何か) は、与えられたイテレータの要素を結合し、それらを 1 つの文字列に変換します。ここで、空文字列 '' が区切り文字として使われています。
        reversed_line = ''.join(reversed(line))
        # ファイルに書き込む
        f.write(reversed_line)
