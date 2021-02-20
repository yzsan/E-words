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
    # .encordingで現在の文字コードを表示させることができる。
    # print(r.encording)
    
    # return

    soup = BeautifulSoup(r.text, features="html.parser")
    # print(soup)


    td_list = soup.find_all("td")
    print(td_list)

if __name__ == "__main__":
    main()
