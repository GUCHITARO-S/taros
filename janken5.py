from random import randint
import sys


def player_hand():
    try:
        p = int(input("1:グー 2:チョキ 3:パー"))
        if p == 0:
            sys.exit()
        if not (1 <= p <= 3):
            raise ValueError
            
        print("Player:", end="")
        print("グー" if p == 1 else "チョキ" if p == 2 else "パー")
        return p

    except ValueError:
        print("1～3を入力してください")
        return player_hand()


def enemy_hand():
    e = randint(1, 3)
    print("CPU:", end="")
    print("グー" if e == 1 else "チョキ" if e == 2 else "パー")
    return e


def judge(p, e):
    flg = False
    winner = False

    if p == e:
        flg = True
    elif (p - e) % 3 == 2:
        print("プレイヤーの勝ち")
        winner = True
    else:
        print("CPUの勝ち")
    return winner, flg


def janken():
    player = player_hand()
    enemy = enemy_hand()
    winner, flg = judge(player, enemy)
    if flg:
        print("\nあいこでしょ！")
        return janken()
    if winner:
        point = True
    else:
        point = False
    return point


def main():
    p_point = 0
    e_point = 0
    limit = 3

    print("…0で終了")
    while p_point < limit and e_point < limit:
        print("ジャンケンポン！")
        point = janken()
        if point:
            p_point += 1
        else:
            e_point += 1
        print(f"Player:{p_point}勝 CPU:{e_point}勝\n")
    print(f"{limit}勝！プレイヤーの勝ち" if p_point == limit else f"{limit}敗！プレイヤーの負け")


if __name__ == "__main__":
    main()
