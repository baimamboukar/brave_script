class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = -1
        self.current_char = None

    def advance(self):
        self.position += 1
        self.current_char = self.text[1] if self.position < len(
            self.text) else None
