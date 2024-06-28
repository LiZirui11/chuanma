# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 11:34
# @Github  : https://github.com/Leaderzhangyi
# @File    : Player.py
# @Software: PyCharm

import random
from CheckWin import win
import copy
from typing import List
from action import action
from checkAction import checkAction
from Color import Color




class Player:
    def __init__(self,name,cards, throw):
        self.name=name
        self.cards = cards
        self.throw = throw  # 定缺
        self.gangflag = 0
        self.pengflag = 0   #碰标记
        self.Hu = 0
        self.pengList = []
        self.gangList = []
        self.tingList=win.updateTingList(self.cards,self.throw)
    
    def show(self):
        print(f"{self.name}的手牌为：")
        Color.print_colored_cards(self.cards)
        print(f"缺为:{self.throw}")
        print(f"{self.name}的碰牌为：{self.pengList}，杠牌为：{self.gangList},听牌为：{self.tingList}")
        print()
        
    def play(self,game_manager):
        self.show()
        card=action.get_newCard(self,game_manager) 
        self.show()
        if card==-1:
            print("本轮流局，游戏结束！")
            return -1
        
        if checkAction.check_Hu(self,card):
            action.Hu(self,card)
            return -1 
                
        else:
            
            if checkAction.check_AnGang(self,card):
                player_input=input("是否选择暗杠？(输入 'yes' 表示暗杠，'no' 表示不暗杠): ")
                if player_input.lower()=='yes':
                    action.AnGang(self,card)
                    self.play(game_manager)
                    
                
            if checkAction.check_BaGang(self,card):
                player_input=("是否选择粑杠？(输入 'yes' 表示粑杠，'no' 表示不粑杠): ") 
                if player_input.lower()=='yes':
                    action.BaGang(self,card)
                    self.play(game_manager)
            return action.play_card(self)
                 
            

           
                
    def wait(self, card):   
        if checkAction.check_Hu(self, card):
            self.show()
            action.Hu(self, card)
            return "Hu"   
        if checkAction.check_Peng(self, card):
            self.show()
            player_input = input(f"{self.name}是否选择碰？(输入 'yes' 表示碰，'no' 表示不碰): ")
            if player_input.lower() == 'yes':
                action.Peng(self, card)
                
                return "Peng"
        if checkAction.check_Gang(self, card):
            self.show()
            player_input = input("f{self.name}是否选择杠？(输入 'yes' 表示杠): ")
            if  player_input.lower() == 'yes':
                action.Gang(self, card)  
                    
                return "Gang"   
            
            
        
        
            

   
  
    

 
        


    def check_Pao(self, tmpCard, card: str, isOther: bool) -> bool:
        return win(self.throw, tmpCard, card, isOther).check()
    
    
    
   
    
    
    def judge(self, other_card): # 用于判定机器人打出的牌
        result = ""
        tmpCard = copy.deepcopy(self.cards)
       
        tmpCard.append(other_card)
        self.isPao = self.check_Pao(tmpCard,other_card,isOther=True) #判定

        if tmpCard.count(other_card) == 3 or tmpCard.count(other_card) == 4 or self.isPao:

            if tmpCard.count(other_card) == 3 and tmpCard.count(other_card) == 4 and self.isPao:
                result = "请选择操作[碰:0 杠:1 胡:2 跳过:3]   输入(0,1,2,3)："
            elif tmpCard.count(other_card) == 3 and self.isPao:
                result = "请选择操作[碰:0 杠:1(不可用) 胡:2 跳过:3]   输入(0,1,2,3)："
            elif tmpCard.count(other_card) == 3:
                result = "请选择操作[碰:0 杠:1(不可用) 胡:2(不可用) 跳过:3]   输入(0,1,2,3)："
            elif self.isPao:
                result = "请选择操作[碰:0(不可用) 杠:1(不可用) 胡:2 跳过:3]   输入(0,1,2,3)："
                print(self.isPao)
            option = input(result)
            while True:
                if option not in ['0','1','2','3']:
                    print("输入有误！请重新输入!")
                    option = input(result)
                elif option == '0':
                    self.Peng(other_card)
                    break
                elif option == '1':
                    # 杠的逻辑
                    self.gangflag = 1
                    self.Gang(card=other_card)
                    break
                elif option == '2':
                    # 加上胡的类型
                    print("你胡了！！游戏结束")
                    self.Hu = 1
                    break
                elif option == '3':
                    break



