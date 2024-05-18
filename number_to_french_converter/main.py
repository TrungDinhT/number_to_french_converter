import typer
from typing_extensions import Annotated

import json

from .number_converter import convert_number

app = typer.Typer()


@app.command()
def convert_numbers_to_french(
    input: Annotated[
        str, typer.Argument(help="Path to file containing numbers to be converted")
    ],
    output: Annotated[str, typer.Option(help="Path to file to save outputs")] = None,
):
    with open(input, "r") as in_file:
        data = json.load(in_file)
        out = {str(number): convert_number(number) for number in data}

        if output is None:
            output = "out.json"
        with open(output, "w") as out_file:
            json.dump(out, out_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    app()
