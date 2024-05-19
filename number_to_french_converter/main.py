import typer
from typing_extensions import Annotated

import json

from .number_converter import convert_number
from .constants import FrenchVariant

app = typer.Typer()


@app.command()
def convert_numbers_to_french(
    input: Annotated[
        str, typer.Argument(help="Path to file containing numbers to be converted")
    ],
    output: Annotated[str, typer.Option(help="Path to file to save outputs")] = None,
    variant: Annotated[FrenchVariant, typer.Option(help="Variant of french to use")] = FrenchVariant.French,
):
    with open(input, "r") as in_file:
        data = json.load(in_file)
        out = {str(number): convert_number(number, variant=variant) for number in data}

        if output is None:
            output = f"out_{variant.value}.json"
        with open(output, "w") as out_file:
            json.dump(out, out_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    app()
