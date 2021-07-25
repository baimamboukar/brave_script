class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __represent__(self):
        if self.value:
            return f'{self.typr}:{self.value}'
        return f'{self.type}'
