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
エラー対応④SyntaxError: EOF while scanning triple-quoted string literal
コメントの閉じが重複していて、main()の )に ^ の警告が。∴エラー時は広く前後を見るべし。あとスペル。
"""

import requests
from bs4 import BeautifulSoup
import time
import random
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

def save_problems():
    """
    スクレイピングして問題を作成、ファイルに保存する。
    """
    
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
    # print(td_values)

    """
    次にこれらの情報をファイルに書き込んでいく。
    with構文とopen関数を使ってファイルを開く。「withを使ってファイルを開くとファイルcloseを省略することができる。」
    適当にwords.txtというファイルに保存することにする。
    書き込みモードWを設定し、for文で回していく。
    先ほどのtd_valueの値をfor文で一つ一つ取得していく。
    ファイルの書き込みはf.でwrite()という関数を使う。\nは改行コード
    """
    # with open("words.txt", "w") as f:
    #     for value in td_values:
    #         f.write(value + "\n")

    # words.txtというファイルが作成され全て一行ずつ書き込みOK
    # これだけだと単語帳作る時に不便が多いのでもう少し加工していく。一旦コメントアウト 。

    """
    リストの中をさらに分けることにする。
    まずは空のリストを宣言する。
    Webページの単語リストにも一行４つの情報が収納されていたので
    ４つずつリストを別のリストに入れることにする。
    これはrange関数を使っていけばできる。
    初めのインデックス、終わりのインデックス、そして何個づつリストを飛ばして読むか
    というのを指定すれば実現することができる。ここでは４を指定する。
    """
    
    splited_list = []

    for index in range(0, len(td_values), 4):
        # print(index)
        # print(td_values[index])
        a = td_values[index: index + 4]

        if a[0] == '\u3000':
            continue
        splited_list.append(a)
        # print(td_values[index: index + 4])

    # print(splited_list)

    """
    実行してみるとインデックスのナンバーと行の番号が表示された。
    これ２つ同時に表示すると訳がわからなくなるのでもう少し修正。
    いったんコメントアウトして行番号だけ表示するようにする。
    (webページの一番左の行番号を表示)
    ４つずつ塊を出すので
    index:index+4を指定する。これはリストのスライス(別途)を使っている。
    実行結果を見ると一行一行リストに入っている。
    途中、表のヘッダーも入っているのでこれは除外と。
    ちょうど行番号の所に空欄の文字コード('\u3000')が入っているので
    これを指定して除外する。
    いったんリストを変数に入れる。変数aとする。
    そしてリストに追加するためにappendをする。
    ヘッダーは除外したいので0番目の要素に文字コードを指定。
    除外するのでcontinueを指定。
    continueを指定することでfor文のループを次にまわすことができる。
    実行するとリストの中にさらにリストが入っている。
    """
    """
    次に先ほど作ったリストを基に書き込みをしていく。
    欲しいのは英単語とその日本語和訳だけなので
    1番目の要素と2番目の要素だけを書き込む。
    最初に1番目の要素、次に2番目の要素を書き込んでみる。
    こうすることで先に英単語、次に日本語訳が表示。
        a 4th grader
        4年生
        a few
        少しの
    """

    # with open("words.txt", "w") as f:
    #     for value in splited_list:
    #         f.write(value[1] + "\n")
    #         f.write(value[2] + "\n")

    """
    この出し方だと先に英単語を出し、次に日本語訳を出す形だけとなる。
    先に日本語訳を出すパターンもあると思うので、行に分けずに一行に英単語とその和訳を表示することにする。
    これはformat関数を使って書く。
    一行ずつ書き込むことができた。
        a 4th grader,4年生
        a few,少しの
    """
    with open("words.txt", "w") as f:
        for value in splited_list:
            f.write("{},{}\n".format(value[1], value[2]))

    """
    次に今までの処理を関数に分けることにする。
    main関数の名前を変える。save_problemsという名前にする。
    そして大まかに関数の中身の内容をコメントで書いておく。
    ダブルクオーテーション三つで複数行のコメントアウトを作成することができる。
    またmain関数を宣言する。
    こちらではテキストファイルを読み込んで問題を表示する部分を書いていく。
    またwithとopenを使う。
    ファイルを開く場合はモードをrとする。
    リードライン関数を使えば一行ごとリストに入れてくれる。
    (表示)
    ['a 4th grader,4年生\n', 'a few,少しの\n', 'a great deal of -,大量の\n', 'a host of,多数の、大勢の\n', 'a hundred -,多数の〜\n', '
    このようにリストに入れることができた。しかし改行が入っている。
    この改行を削除していく。（これ間違ってスピリット関数を使った。後で訂正する。
    正しくはストリップ(strip)関数。
    (表示)
    ['a 4th grader,4年生', 'a few,少しの', 'a great deal of -,大量の', 'a host of,多数の、大勢の', 'a hundred -,多数の〜', 
    改行コードを削除することができた。
    
    その中身を一つ表示させてみる。
    split関数を使うとカンマで分けることができる。
    分けた結果はリストで返してくれる。
    （表示）最後breakありなのでこれだけを表示↓
        a 4th grader,4年生
        ['a 4th grader', '4年生']

    0番目の要素が英単語
    1番目の要素が日本語訳になる。
    (表示)するとこのように表示できた。
        a 4th grader
        4年生
        a few
        少しの
    """
    
    """
    ＊＊＊＊＊＊　ここからmain_random.py　＊＊＊＊＊＊
    まず問題を取得する関数を書く。def get_problems()
    これをファイル読み込みしてリストに突っ込むとこまでを関数に書く。
    （def mainの実行文をカットしてペースト with〜）
    問題のリストを返す。return problems
    """
def get_problems():
    """
    ファイルから問題と回答のリストを返す
    return 問題と回答のリスト
    """
    with open("words.txt", "r") as f:
        problems = f.readlines()
        # print(problems)
        problems = [x.strip() for x in problems]

    return problems

    """
    ＊＊＊＊＊＊　続き　＊＊＊＊＊＊
    次にリストを受け取って、問題を表示する部分の関数も書いていく。
    main関数の中身をごっそり移動させる。
    引数は問題のリストにする。
    大まかな関数の内容をコメントで書いておく。
    プログラム書いた本人も時間が経つと内容は忘れてしまう。
    なのでコメントを書くことは重要。
    def start_english_words_test とともに def get_problemsにも。
    関数に分けて書いて実行できるか確かめてみる。
    問題なく実行できた。
    次にランダムで出すためにimport randomしておく。
    受けとったリストをランダムでシャッフルする。
    random.shuffleを使えばできる。
    リストを渡せばリストの中身をシャッフルしてくれる。
    これで問題をランダムで出題することができる。
    実際に確認。
    main_random.pyを実行すること忘れずに！
    これで短時間で多くの単語を復習したり覚えたりすることができる。
    このようにスクレイピングによってデータを用意し、そんデータを加工しそれを表示することで単語テストを作ることができた。
    今回は英単語のデータを使ってアプリケーションを作った。
    Pythonの基本的な文法にて。　
    """
def start_english_words_test(problems):
    """
    単語テストを開始する
    英単語と日本語訳を表示
    """
    for index, p in enumerate(problems):
        # print(p)
        x = p.split(",")
        # print(x)
        # break

        english = x[0]
        japanese = x[1]
        print("====第{}問目===".format(index + 1))

        print(english)
        time.sleep(1)
        print(japanese)
        time.sleep(0.5)
        # break




def main():
    p = get_problems()
    random.shuffle(p)
    start_english_words_test(problems=p)

        # print(problems[0:10])
        
        # for index, p in enumerate(problems):
        #     # print(p)
        #     x = p.split(",")
        #     # print(x)
        #     # break

        #     english = x[0]
        #     japanese = x[1]
        #     print("====第{}問目===".format(index + 1))

        #     print(english)
        #     time.sleep(1)
        #     print(japanese)
        #     time.sleep(0.5)
        #     # break

    """
    以下strip関数であれば問題なし。
    （一見改行コードがなくなってつように見えるけどこれは間違い。
    （split関数に引数が指定されていない場合、空白毎に要素を挙げてしまう。
    （カンマで分かれているので、それをスピリット関数で分けていく。
    （split関数の引数にカンマを指定する。
    （要素一つだけ見たいのでbreakでfor文を止める。
    """
            # for p in problems:
            #     print(p)
            #     x = p[0].split(",")
            #     print(x)
            #     break
    """
    出題の演出
    英単語を表示して少し待ってから日本語訳を表示させてみる。
    この少し待つというところでtimeを使う。import time
    次にtime.sleepで待つ秒数を指定する。2秒待つことにする。
    こうすることで単語テストを表示することができた。

    今日本語訳が出てすぐ次の問題が出てしまっている。これを修正する。
    これ日本語訳が出てからも待つことにすればよい。
    もう一行time.sleepを使う。

    次に今、何問目かも表示させる。
    enumerate関数を使えば、for文のインデックスを取得することができる。
    for p in problems: >> for index, p in enumerate(problems):
    このインデックスを使って今何問目かを表示させる。
    0問目となってたので(print側のコードで)+1にする。インデックスは0から始まるのでこのようなことが起こる。
    """
    """
    少し難しくするために間隔の秒数を短くする。1と0に
    これで素早く表示させることができる。
    """


if __name__ == "__main__":
    main()
