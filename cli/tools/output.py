import typing

import click


class Square:
    angle: int = 4

    def __init__(self, strings: typing.List[str], color: str = "red"):
        self.strings = strings
        self.color = color

    @property
    def long_word(self):
        return max([len(i) for i in self.strings])

    @property
    def length(self):
        return self.long_word + 4

    @property
    def str_length(self):
        return f"+{'-' * self.length}+"

    def draw(self):
        click.echo(click.style(self.str_length, fg=self.color))
        for string in self.strings:
            output_str = (
                f"| {string + ' ' * (len(self.str_length) - len(string) - 4)} |"
            )
            click.echo(click.style(output_str, fg=self.color))
        click.echo(click.style(self.str_length, fg=self.color))
