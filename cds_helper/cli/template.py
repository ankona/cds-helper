import argparse
import json
import pathlib


def help_text() -> str:
    """Return subparser help text."""
    return "Generate a template input file for customization"


def command() -> str:
    """Return subparser command name."""
    return "template"


def configure_parser(parser: argparse.ArgumentParser) -> None:
    """Configure the parser for this sub-command."""
    parser.add_argument(
        "-publisher",
        help="Specify the dataset publisher.",
        default="cds",
        choices=["cds"],
    )
    parser.add_argument("path", help="The path to the desired output file.")


def handle(args: argparse.Namespace) -> None:
    """Process a CLI request."""
    template = {
        "dataset": "dataset-name",
        "start_date": "2027-01-01",
        "end_date": "2027-12-31",
        "variables": [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "sea_surface_temperature",
            "total_precipitation",
            "surface_net_solar_radiation",
            "surface_thermal_radiation_downwards",
        ],
    }

    output_path = pathlib.Path(args.path)
    with output_path.open("w") as fp:
        json.dump(template, fp, indent=4)
