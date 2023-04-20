class Color:
    def __init__(self, color, text) -> None:
        self._color = color
        self._text = text

    @property
    def __green(self):
        return "\033[92m" + self._text + "\033[0m"
    
    @property
    def __yellow(self):
        return "\033[93m" + self._text + "\033[0m"
    
    @property
    def __red(self):
        return "\033[91m" + self._text + "\033[0m"
    
    def __str__(self) -> str:
        if self._color == "green":
            return self.__green
        elif self._color == "yellow":
            return self.__yellow
        else:
            return self.__red