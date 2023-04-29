#モジュールインポート
import random
import time

#ジャンケンの手を配列に
jan = ["グー", "チョキ", "パー"]

jan_count = 0
win_count = 0

while True:
    myjan_int = -99
    jan_result = -99
    con_result = -99 

    while True:

        #自分のジャンケンの手を決める
        print("何を出すか決めて、数字を入力してね。")
        print("[グーなら1を入力 / チョキなら2を入力 / パーなら3を入力]")
        myjan_int = int(input()) - 1
        print("")

        while myjan_int < 0 or myjan_int >2:
            print("数字が間違ってるよ。もう一度入力してね。")
            myjan_int = int(input()) - 1
            print("")
                

        #相手のジャンケンの手を決める
        pcjan_int = random.randint(0, 2)

        #ジャンケンの勝負
        print("さあ、勝負！！")
        print("じゃーんけん")
        time.sleep(1)
        print("")
        print("ぽん！！")
        print("")
        print("あなたが出したのは【" + jan[myjan_int] + "】")
        print("あいてが出したのは【" + jan[pcjan_int] + "】")
        print("")

        #勝敗計算 (結果が0ならあいこ、-1か2なら勝ち、-2か1なら負け)
        jan_result = myjan_int - pcjan_int

        if jan_result == 0:
            print("★★ あいこ！もう一回！！ ★★")
            print("")
        elif jan_result == -1 or jan_result == 2:
            print("★★ あなたの勝ち！すごい！ ★★")
            print("")
            jan_count = jan_count + 1
            win_count = win_count + 1
            break
        elif jan_result == -2 or jan_result == 1:
            print("★★ あなたの負け。ざんねん＞＜ ★★")
            print("")
            jan_count = jan_count + 1
            break


    while con_result < 0 or con_result > 1:
        print("もう一回やる？数字を入力してね")
        print("[やるなら 1 / やめるなら 0]")
        con_result = int(input())
        
        if con_result < 0 or con_result > 1:
            print("数字が間違ってるよ。もう一度入力してね。")

    if con_result == 1:
        print("")
        print("よし！もう一回だね")
        print("")
        print("")
    elif con_result == 0:
        print("")
        print("またやってね！")
        break
        


#勝敗結果
print("")
print("◆+--------------+--------------+◆")
print("【じゃんけんの結果】")
print("    じゃんけんを "+ str(jan_count) + " 回やって " + str(win_count) + " 回勝ったよ")
print("◆+--------------+--------------+◆")












