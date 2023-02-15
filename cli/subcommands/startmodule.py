import pathlib

import click
import jinja2

from scripts.cli.tools.color_string_builder import *
from scripts.constants import APPLICATIONS_FOLDER, TEMPLATE_FOLDER, TESTS_FOLDER

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_FOLDER / "startmodule")
)


def template_from_string(string: str, module_name: str):
    t = jinja2.Environment().from_string(string)
    return t.render(module_name=module_name)


def create_file(
    template_path: pathlib.Path,
    module_name: str,
    src_path: pathlib.Path = APPLICATIONS_FOLDER,
):
    template_path = pathlib.Path(template_path.parent.name, template_path.name)
    file_name = template_path.name.strip(".jinja")
    t = env.get_template(template_path.as_posix())
    src_path = src_path / file_name
    src_path.touch(exist_ok=True)
    src_path.write_bytes(t.render(module_name=module_name).encode())


def create_module(
    template_path: pathlib.Path,
    module_name: str,
    src_path: pathlib.Path = APPLICATIONS_FOLDER,
):
    for file in template_path.iterdir():
        if file.is_dir():
            module_name = template_from_string(file.name, module_name)
            src_path = src_path / module_name
            src_path.mkdir(parents=True)
            create_module(file, module_name, src_path=src_path)
            src_path = src_path.parent
        else:
            create_file(file, module_name, src_path=src_path)


def create_test_module(module_name: str):
    tests_path = TESTS_FOLDER / module_name
    tests_path.mkdir()
    init_file = tests_path / "__init__.py"
    init_file.touch()


@click.command("startmodule")
@click.argument("module_name", type=str)
def startmodule(module_name: str):
    templates_folder = TEMPLATE_FOLDER / "startmodule"
    module_name = module_name.lower()
    create_module(templates_folder, module_name)

    echo_text = [
        ColorString("\u2714 Module", Colors.GREEN),
        ColorString(module_name, Colors.YELLOW),
        ColorString("created", Colors.GREEN),
    ]

    click.echo(ColorStringBuilder.build(echo_text))

    create_test_module(module_name)

    echo_text = [
        ColorString("\u2714", Colors.GREEN),
        ColorString(module_name, Colors.YELLOW),
        ColorString("added to tests", Colors.GREEN),
    ]

    click.echo(ColorStringBuilder.build(echo_text))
