
# action.py
from CheckWin import win

class action:
    
    # 摸牌
    @staticmethod
    def get_newCard(player, game_manager):
        if game_manager.AllMa:  # 确保牌堆非空
            card = game_manager.AllMa.pop(0)  # 从牌堆中取出牌
            print(f"{player.name}摸到了: {card}")
            player.cards.append(card)
            player.cards.sort(key=lambda x: (x[1], x[0]))
            print(f"牌库还剩下{len(game_manager.AllMa)}张牌。")
            return card
        else:
            print("牌堆中没有牌了。")
            return -1
    #打牌
    @staticmethod    
    def play_card(player):
        while True:
            out = input("请你打出一张牌：")
       
            if out in player.cards:
            # 从手牌中移除玩家指定的牌
                player.cards.remove(out)
                print(f"你打出了一张 {out}")
                player.tingList=win.updateTingList(player.cards,player.throw)
                return out
            else:
            # 如果手牌中没有指定的牌，提示错误并要求重新输入
                print(f"错误：手牌中没有 {out}，请重新选择一张牌打出。")
    #胡牌    
    @staticmethod        
    def Hu(player,card):
        player.Hu = 1
        print(f"{player.name}胡了！！游戏结束")
        
    #暗杠
    @staticmethod    
    def AnGang(player, card):
        print(f"你暗杠了 {card}")   
        gang_list = [card] * 4
        player.gangList.append(gang_list)
        for _ in range(4):
            player.cards.remove(card)
        player.gangflag = 1 #杠标记为 1 
    #粑杠 
    @staticmethod   
    def BaGang(player, card):
        print(f"你粑杠了 {card}")
        for pengCards in player.pengList:
            if card in pengCards:
                player.pengList.remove(pengCards)  # 从碰牌列表移除
                break
        gang_list = [card] * 4
        player.gangList.append(gang_list)
        player.cards.remove(card)  # 从手牌中移除该张牌，因为摸到的牌已经用于粑杠，所以只需移除一次
        player.gangflag = 1  # 杠标记设置为 1
        
    @staticmethod    
    def Peng(player, card: str):
        peng_list = [card] * 3
        player.pengList.append(peng_list)
        for _ in range(2):
            player.cards.remove(card)
        
    @staticmethod
    def Gang(player, card):
        
        print(f"你杠了 {card}")   
        gang_list = [card] * 4
        player.gangList.append(gang_list)
        for _ in range(3):
            player.cards.remove(card)
        player.gangflag = 1 #杠标记为 1    
        

    
            
        
        
        
    