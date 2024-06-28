# __init__.py

from game_manager import GameManager

def GameStart():
    # 创建游戏管理器实例
    game_manager = GameManager()
    # 开始游戏
    game_manager.GameControl()

if __name__ == "__main__":
    GameStart()