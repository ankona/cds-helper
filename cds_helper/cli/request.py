import argparse


def help_text() -> str:
    """Return subparser help text."""
    return (
        "Retrieve data by specifying a path to a "
        "JSON file containing the request parameters."
    )


def command() -> str:
    """Return subparser command name."""
    return "request"


def configure_parser(parser: argparse.ArgumentParser) -> None:
    """Configure the parser for this sub-command."""
    parser.add_argument("file", help="Path to a file containing request details.")


def handle(args: argparse.Namespace) -> None:
    """Process a CLI request."""
    print("empty request handler")
