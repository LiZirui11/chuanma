# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 22:24
# @Github  : https://github.com/Leaderzhangyi
# @File    : CheckWin.py
# @Software: PyCharm
import copy
from collections import Counter
import unittest

class win:
    AllType = [str(i) + j for i in range(1, 10) for j in ("万", "条", "筒")]
    AllType.sort(key=lambda x: (x[1], x[0]))

    @staticmethod
    def run(temp, throw, count, hasRun):
        """
        :param temp: 临时字典变量
        :param throw: 扔掉的牌
        :param count: 牌组数量
        :param hasRun: 是否判断对子
        :return: bool变量
        """
        if count == 0:
            return True  # 可以胡牌
        if not hasRun:
            for num in win.AllType:
                if temp[num] >= 2 and num[1:] != throw:
                    temp[num] -= 2
                    if win.run(temp, throw, count - 2, True):
                        return True
                    temp[num] += 2
            return False
        else:
            for num in win.AllType:
                if num[1:] != throw and temp[num] > 0:
                    if temp[num] >= 3:  # 刻子
                        temp[num] -= 3
                        if win.run(temp, throw, count - 3, True):
                            return True
                        temp[num] += 3
                    if int(num[0]) + 2 <= 9 and temp[str(int(num[0]) + 1) + num[1]] > 0 and temp[
                        str(int(num[0]) + 2) + num[1]] > 0:
                        temp[num] -= 1
                        temp[str(int(num[0]) + 1) + num[1]] -= 1
                        temp[str(int(num[0]) + 2) + num[1]] -= 1
                        if win.run(temp, throw, count - 3, True):
                            return True
                        temp[num] += 1
                        temp[str(int(num[0]) + 1) + num[1]] += 1
                        temp[str(int(num[0]) + 2) + num[1]] += 1
            return False

    @staticmethod
    def updateTingList(cards, throw):
        '''更新听牌列表'''
        tingList = []  # 创建一个空列表来存储听牌
        
        # 方法内部的逻辑
        temp = Counter(cards)
        temp_copy = copy.deepcopy(temp)
        for elem in win.AllType: 
            if temp[elem] < 4 and elem[1:] != throw:
                temp[elem] += 1
                temp_copy = copy.deepcopy(temp)
                if win.run(temp_copy, throw, len(cards) + 1, False):
                    tingList.append(elem)
                temp[elem] -= 1
        
        return tingList
    
    
    
    
    
class TestWinAlgorithm(unittest.TestCase):

    def test_ting_list(self):
        # 准备测试数据，例如一组可以听牌的麻将牌组
        cards=['1万', '2万', '3万', '4万', '5万', '6万','7万','7万','2条','3条']
        cards2=['1万', '2万', '3万', '4万', '5万', '6万','7万','7万','2条','3条','4条']
        # 调用听牌算法，更新听牌列表
        throw = '筒'  # 假设扔掉的牌是'5筒'
        temp = Counter(cards2)
        if win.run(temp, throw, len(cards2), False):
            print("可以胡牌")
        else:
            print("不能胡牌")    
            
        actual_ting_list = win.updateTingList(cards, throw)
        print(actual_ting_list)
      
        # 预期听牌列表应该是一些特定的牌型，根据实际情况进行断言
        expected_ting_list = ['1条','4条']        
        self.assertListEqual(actual_ting_list, expected_ting_list)

if __name__ == '__main__':
    unittest.main()