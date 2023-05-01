import random

win = 0
draw = 0
print("じゃんけんをしましょう！")

for i in range(3):
    print("Round" + str(i + 1))
    print("> 0: グー, 1: チョキ, 2: パー")

    com = random.randint(0, 2)
    you = int(input("あなたの手は？"))

    print("コンピュータの手は" + str(com))

    #じゃんけんの判定
    n = (com - you + 3) % 3

    if n == 0:
        print("あいこです")
        draw += 1
    elif n == 1:
        print("あなたの勝ちです")
        win += 1
    else:
        print("あなたの負けです")
    print("-------")

#最終結果
print("結果は3戦" + str(win) + "勝" + str(draw) + "引き分け")