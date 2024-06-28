from colorama import Fore, Style
class Color:
    @staticmethod
    def print_colored_cards(cards):
        colored_cards = []
        for card in cards:
            if '万' in card:
                colored_card = f"{Fore.RED}{card}{Style.RESET_ALL}"
            elif '条' in card:
                colored_card = f"{Fore.GREEN}{card}{Style.RESET_ALL}"
            elif '筒' in card:
                colored_card = f"{Fore.BLUE}{card}{Style.RESET_ALL}"
            else:
                colored_card = card
            colored_cards.append(colored_card)

        print(' '.join(colored_cards))  # 以空格分隔，同一行显示


# 普通的牌列表
cards = ['1万', '1条', '9筒']

# 调用函数打印带颜色的牌在同一行上显示
Color.print_colored_cards(cards)