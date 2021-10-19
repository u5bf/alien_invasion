import json

class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态。
        self.game_active = False
        # 任何情况都不应修改最高得分。
        self._read_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self):
        """读取 json 文件的最高分."""
        filename = 'highscore.json'
        try:
            with open(filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
            self._write_high_score(self.high_score)

    def _write_high_score(self, high_score):
        """将最高分写入 json 文件中."""
        filename = 'highscore.json'
        with open(filename,'w') as f:
            json.dump(high_score, f)