from enum import Enum

import click


class Colors(Enum):
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    RED = "RED"


class ColorString:
    def __init__(self, string: str, color: Colors) -> None:
        self.string = string
        self.color = color.value.lower()

    def __repr__(self) -> str:
        return click.style(self.string, fg=self.color)

    def __str__(self) -> str:
        return click.style(self.string, fg=self.color)


class ColorStringBuilder:
    @staticmethod
    def build(string_list: list[ColorString], separator=" "):
        string_list = list(map(str, string_list))
        return separator.join(string_list)
