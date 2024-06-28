# game_manager.py

import random
from Player import Player
from Color import Color
from action import action
class GameManager:
    def __init__(self):
        self.Cards, self.AllMa = self.CardInit()
    
    def CardInit(self):
        Cards = {(str(i) + unit): 4 for i in range(1, 10) for unit in ["万", "条", "筒"]}
        AllMa = list(Cards.keys()) * 4
        random.shuffle(AllMa)
        return Cards, AllMa
    
    def GameControl(self):
        self.table_cards={}
        print("对局开始，正在初始化数据".center(50, '='))
        # 发牌
        print("发牌中...")
        init_cards = []
        for i in range(0, 52, 13):
            init_cards.append(self.AllMa[i:i + 13])
        for item in init_cards:
            for j in item:
                self.Cards[j] -= 1

        # 创建4个玩家实例
        players = [Player(name="Player" + str(i + 1), cards=init_cards[i], throw="") for i in range(4)]
        
        self.AllMa = self.AllMa[52:]  # 更新牌库
        print(f"发牌完成！牌库还有{len(self.AllMa)}张")
        banker_index=random.randint(0,3)
        banker=players[banker_index]    
        
        
        print(f"{banker.name}被选为庄家。")
        
        for player in players:
            player.cards.sort(key=lambda x: (x[1], x[0]))
            print(f"{player.name}的手牌为：")
            Color.print_colored_cards(player.cards)
            print(f"{player.name},请定缺：")
            while True:
                throw=input("请选择缺一门：万、条、筒：")
                if throw in ["万", "条", "筒"]:
                    break
                else:
                    print("输入错误，请重新输入！")   
                    
            player.throw=throw
            print(f"{player.name}定缺{throw}成功！")
    
        current_player_index = banker_index
        
        
        pengFlag=0
        while True:
            current_player = players[current_player_index]
            if pengFlag==1:
                played_card=action.play_card(current_player)
                pengFlag=0 
            else:    
                played_card = current_player.play(self)
            if played_card == -1:  # 表示庄家或者当前玩家已经胡牌
                print(f"{current_player.name}胡牌，游戏结束。")
                break
                
            action_taken=False
            for player in players:
                if player != current_player:
                    result = player.wait(played_card)
                    if result == "Hu":
                        print(f"{player.name}胡了！游戏结束。")
                        return
                    elif result in ["Peng", "Gang"]:
                        current_player_index = players.index(player)
            
                        action_taken=True    
                        if result == "Peng":
                            pengFlag=1
                        break
            if not action_taken:
                current_player_index = (current_player_index + 1) % len(players)
                            

           
        