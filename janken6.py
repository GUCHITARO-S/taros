from random import randint


class janken:
    
    def __init__(self, name):
        self.name = name
        self.hand = "" 
        self.win = 0
        self.lose = 0
        self.draw = 0


    def choose_hand(self): 
        hand = {1: "グー", 2: "チョキ", 3: "パー", 0: "end"}

        if self.name:
            try:
                hand_input = int(input("1:グー 2:チョキ 3:パー  0:終了  4:戦績"))
    
                if 0 <= hand_input <= 3: 
                    self.hand = hand[hand_input]
                elif hand_input == 4:
                    self.show_data()
                    return self.choose_hand()
                else:
                    print("1-3の数字を入力してください。" + "\n")
                    return self.choose_hand()

            except ValueError:
                print("数字を入力してください。" + "\n")
                return self.choose_hand()
        else:
            self.hand = hand[randint(1, 3)]

    
    def show_data(self):
        print(f"{self.win}勝{self.lose}敗{self.draw}分" + "\n")


    @classmethod
    def judge(cls, player, enemy): 
        if player.hand == enemy.hand:
            player.draw += 1
            enemy.draw += 1
            return "あいこ"
        elif ((player.hand == "グー" and enemy.hand == "チョキ") or
              (player.hand == "チョキ" and enemy.hand == "パー") or
              (player.hand == "パー" and enemy.hand == "グー")):
            player.win += 1
            enemy.lose += 1
            return "プレイヤーの勝ち"
        else:
            player.lose += 1
            enemy.win += 1
            return "CPUの勝ち"

   

def main():
    print("じゃんけん開始")
    player = janken(True)
    enemy = janken(False)

    while True:
        player.choose_hand()
        if player.hand == "end":
            print("じゃんけん終了")
            break
        enemy.choose_hand()
        result = janken.judge(player, enemy)
        print(result + "\n")


if __name__ == "__main__":
    main()
