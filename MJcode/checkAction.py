


class checkAction:
    
    @staticmethod
    def check_Hu(player,card):
        if card in player.tingList:
            return True 
        return False
    @staticmethod    
    def check_BaGang(player, card):
       
        for pengCard in player.pengList:
            if card in pengCard:
                return True
        return False
    
    @staticmethod
    def check_AnGang(player, card):
        count = player.cards.count(card)
        if count == 4:
            return True
        else:
            return False 
    @staticmethod
    def check_Gang(player, card):
        count = player.cards.count(card)
        if count == 3:
            return True
        else:
            return False     
        
    @staticmethod    
    def check_Peng(player,card):
        count=player.cards.count(card)
        if count==2:
            return True 
        else:
            return False
             
        
        
                