import csv

quiz_pattern = ["ポケモンクイズ", "クレヨンしんちゃんクイズ", "鬼滅の刃クイズ"]
quiz_file_list = ["quiz_pokemon.csv", "quiz_shinchan.csv", "quiz_kimetsu.csv"]


# どのクイズをするのか選択
print("どのクイズをするのか選んでね")
for i in range(len(quiz_pattern)):
    print( str(i+1) + ":" + quiz_pattern[i])

p = int(input()) - 1

quiz_filename = quiz_file_list[p]

# 選択したクイズの問題リストを取得
quiz = open(quiz_filename, 'r', encoding = 'utf8')
quizlist = list(csv.reader(quiz))
quiz.close()

# 問題数を取得
for quiz_count, _ in enumerate(quizlist,1):
    pass

# クイズメイン処理
ans_count = 0
print("\nえらんだクイズは" + quiz_pattern[p])
print("クイズは全部で" + str(quiz_count) + "問!")
for i in range(quiz_count):
    print("\n" + str(i+1) + "番目の問題!!")
    print(quizlist[i][0])
    print("1:" + quizlist[i][1] + "/ 2:" + quizlist[i][2] + "/ 3:" + quizlist[i][3])
    ans = input()
    if ans == quizlist[i][4]:
        print("正解\n")
        ans_count = ans_count + 1
    else:
        print("不正解\n")   

# 結果発表
print("結果発表!! あなたは")
print(str(quiz_count) + "問中" + str(ans_count) + "問正解だよ")
print("またやってね")

