class janken:
    
    def __init__(self, name):
        self.name = name
        self.player_hand = "" 
        self.win = 0
        self.lose = 0
        self.draw = 0


    def choose_hand(self): 
        if self.name:
            try:
                hand_input = int(input("1:グー 2:チョキ 3:パー  0:終了  4:戦績"))
                if hand_input == 0:
                    return "end" 
                elif hand_input == 4:
                    self.show_data()
                    return self.choose_hand()
                elif hand_input == 1:
                    self.player_hand = "グー"
                elif hand_input == 2:
                    self.player_hand = "チョキ"
                elif hand_input == 3:
                    self.player_hand = "パー"
                elif not (0 <= hand_input <= 3): 
                    print("1-3の数字を入力してください。" + "\n")
                    return self.choose_hand()
            except ValueError:
                print("数字を入力してください。" + "\n")
                return self.choose_hand()
        else:
            from random import randint
            hand = {1: "グー", 2: "チョキ", 3: "パー"}
            self.player_hand = hand[randint(1, 3)]

    
    def show_data(self):
        print(f"{self.win}勝{self.lose}敗{self.draw}分" + "\n")


    @classmethod
    def judge(cls, player, enemy): 
        if player.player_hand == enemy.player_hand:
            player.draw += 1
            enemy.draw += 1
            return "あいこ"
        elif ((player.player_hand == "グー" and enemy.player_hand == "チョキ") or
              (player.player_hand == "チョキ" and enemy.player_hand == "パー") or
              (player.player_hand == "パー" and enemy.player_hand == "グー")):
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
        player_result = player.choose_hand()
        if player_result == "end":
            print("じゃんけん終了")
            break
        enemy.choose_hand()
        result = janken.judge(player, enemy)
        print(result + "\n")


if __name__ == "__main__":
    main()
