class Setting:
    def __init__(self, num_cols: int, num_rows: int, num_bombs: int, name: str):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.num_bombs = num_bombs
        self.name = name

    def match_name(self, given: str):
        return self.name.lower() == given.lower()


class Settings: 
    settings = [
        Setting(5, 5, 4, 'easy'),
        Setting(10, 10, 9, 'medium'),
        Setting(16, 16, 15, 'hard')
    ]

    @classmethod
    def select(cls, arg):
        for setting in cls.settings:
            if setting.match_name(arg):
                return setting