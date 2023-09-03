import random

count = 0


def janken(ch_hand: int) -> tuple[int, str]:
    hands = {1: "グー", 2: "チョキ", 3: "パー"}
    hand = (ch_hand, hands[ch_hand])
    return hand


def judge(player, enemy: [tuple[int, str], ...]) -> None:
    global count
    if count > 0:
        print("あいこでしょ")
    else:
        print("じゃんけんぽん")
    print(f"py -> {player[1]} : cp -> {enemy[1]}")
    if player[0] == enemy[0]:
        count = 1
    elif player[0] - enemy[0] == -1 or player[0] - enemy[0] == 2:
        print("プレイヤーの勝ち")
        count = 0
    else:
        print("CPUの勝ち")
        count = 0


def main():
    while True:
        try:
            py = int(input("1: グー , 2: チョキ 3: パー -> 0 で終了 => "))
            if py == 0:
                break
            if not 0 < py < 4:
                continue
        except (ValueError, EOFError) as e:
            print(type(e))
            continue
        cp = random.randint(1, 3)
        enemy_hand = janken(cp)
        player_hand = janken(py)
        judge(player_hand, enemy_hand)


if __name__ == "__main__":
    main()
