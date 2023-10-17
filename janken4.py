import sys
import random


def judge(x: int, y: int) -> tuple[bool, int]:
    result: bool = 1
    win: int = 0
    if x == y:
        result = 0
    elif (x - y) % 3 == 2:
        win = 1
        print("プレイヤーの勝ち")
    else:
        print("CPUの勝ち")
    return result, win


def janken(flag) -> tuple[bool, int]:
    flag = flag
    win = 0
    while True:
        try:
            hands = {1: "グー", 2: "チョキ", 3: "パー"}
            player = int(input("じゃんけん！… 1->グー 2->チョキ 3->パー\n"
                               if flag else
                               "あいこで！… 1->グー 2->チョキ 3->パー\n"))
            if player == 0:
                sys.exit()
            if not 1 <= player <= 3:
                raise ValueError
        except ValueError:
            print("1, 2, 3 を入力")
            continue

        enemy = random.randint(1, 3)
        print(f"ぽん！… プレイヤー：{hands[player]}、CPU：{hands[enemy]}"
              if flag else
              f"しょ！… プレイヤー：{hands[player]}、CPU：{hands[enemy]}")
        flag, win = judge(player, enemy)
        return flag, win


def main():
    flag = 1
    count = 0
    print("0 で終了")
    while count < 3:
        flag, win = janken(flag)
        if win:
            count += win
        elif not flag:
            pass
        else:
            count = 0
    else:
        print("３連勝！ヤッピー！")


if __name__ == "__main__":
    main()
