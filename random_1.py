import random
import time

a = 0
b = 0
goal = 20
user = input ("aとbのどちらのカメが勝つか予想してください。")

print("競争開始！")

while (a < goal) and (b < goal):
    print("----")
    a = a + random.randint(1, 6)
    b = b + random.randint(1, 6)
    print("a:" + ">" * a + "@")
    print("b:" + ">" * b + "@")
    if (a > b):
        print("aが優勢です")
    elif (a < b):
        print("bが優勢です")
    else:
        print("同じ位置です")
    time.sleep(1)

if a == b:
    winner = "同時"
elif a < b:
    winner = "a"
else:
    winner = "b"

if winner == user:
    print("あなたの予想は正解です。")
else:
    print("あなたの予想は不正解です。")