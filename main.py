"""
やること
1 英単語のデータを用意。スクレイピングして集める。
2 データを加工
3 データを見やすい形で表示
4 テストの問題に見せる演出
"""

"""
まずmain.pyのファイルを作成。そして英単語のデータをスクレイピングする。
ちょうどテーブル（HTMLのtableタグ）になっているのでそれをスクレイピング
まずbeautifulsoupをインストール（済）
¥ pip install beautifulsoup4
Pythonは3.8.2を使っている。3系なら今回紹介するコードは動く。
次にリクエスツ・ライブラリ、ビューティフル・スープをインポート。
これらのライブラリを使うとウェブ・ページから情報をスクレイピングすることができる。

"""
"""
エラー対応①SyntaxError: Non-ASCII character '\xe3' in file main.py on line 3, but no encoding declared
# -*- coding: utf-8 -*-（Snake2より）
エラー対応②ImportError: No module named requests
python3.8 main.py (Snake2より)
エラー対応③IndentationError: unexpected indent（td_list =)
後のmain()までのインデントを見越して点検。結果returnが前で効いて分断していた。
"""

import requests
from bs4 import BeautifulSoup

"""
次にmain関数を宣言する。
main関数に処理の内容を書いて行く。
まずページURLを入力（URLをペースト）
次にリクエスト・ライブラリを使ってウェブページを取得する。
getリクエストをページURLに対して送る。
次にビューティフル・スープの変数soupを宣言。
ビューティフル・スープに先ほどrequestsで取得したテキストを渡し、それをパース（解析）していく。
こちらはhtmlパーサーを使う。
試しにターミナルで実行してみる。python main『3.8』.py
>> HTMLの内容が表示。一部文字化けは後で直す。
"""

def main():
    page_url = "http://www7b.biglobe.ne.jp/~browneye/english/TOEIC400-1.htm"

    r = requests.get(page_url)

    # 文字コードを確認。リクエスト・ライブラリの機能を使う。
    # .encodingで現在の文字コードを表示させることができる＊＊codingにrは要らない！
    # print(r.encoding)
    # ISO-8859-1 これが文字化けの原因。正しい文字コードを設定する。
    # apparent encoding を使えば本来取得するべきだった文字コードが出てくる。
    # print(r.apparent_encoding)
    # これは SHIFT_JIS が表示されたのでこの SHIFT_JIS を設定する。
    # これは単純にr.encodingにr.apparent_encordingを代入する。
    # print(soup)で実行確認。文字化け直る。print(td_list)でもOK

    r.encoding = r.apparent_encoding
    # return　リターンを入れているのはここで終了という意味「ある関数に置いてreturn以降の行は実行されません」

    soup = BeautifulSoup(r.text, features="html.parser")
    
    # print(soup)

    # return

    td_list = soup.find_all("td")
    # print(td_list)

    # 次にtdタグの中身を取ってくる。
    # .textを使えばtdタグの中身を取ることができる。リストの内包記法を使う。for文を簡単に書くことができる。
    td_values = [x.text for x in td_list]
    print(td_values)

    """
    次にこれらの情報をファイルに書き込んでいく。
    with構文とopen関数を使ってファイルを開く。「withを使ってファイルを開くとファイルcloseを省略することができる。」
    適当にwords.txtというファイルに保存することにする。
    書き込みモードWを設定し、for文で回していく。
    先ほどのtd_valueの値をfor文で一つ一つ取得していく。
    ファイルの書き込みはf.でwrite()という関数を使う。\nは改行コード
    """
    with open("words.txt", "w") as f:
        for value in td_values:
            f.write(value + "\n")

    # words.txtというファイルが作成され全て一行ずつ書き込みOK
    # これだけだと単語帳作る時に不便が多いのでもう少し加工していく。

if __name__ == "__main__":
    main()
