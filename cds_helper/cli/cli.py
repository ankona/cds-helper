"""CDS API - Multi-month Data Retrieval Demo."""

# ruff: noqa: DTZ001
import argparse
import logging
import sys

# def get_file_usage() -> str:
#     return textwrap.dedent(
#         """\
#             >>> python -m ./sample.py retrieve -f ./cds-request.json
#             >>>
#         """
#     )


def create_parser() -> argparse.ArgumentParser:
    """Create a parser for the arguments to this utility."""
    parser = argparse.ArgumentParser(
        "cds-helper",
        description=(
            "cds-helper is a utility for retrieving a contiguous set of monthly "
            "data from the `Climate Data Store` API"
        ),
        # prefix_chars=["-", "--"]
    )

    subparsers = parser.add_subparsers()

    # build cds-helper request <options>
    request_parser = subparsers.add_parser(
        "request",
        help=(
            "Retrieve data by specifying a path to a "
            "JSON file containing the request parameters."
        ),
    )
    request_parser.add_argument(
        "file", help="Path to a file containing request details."
    )

    # build cds-helper get <options>
    get_parser = subparsers.add_parser(
        "get",
        help=("Retrieve data by specifying parameters for a single dataset "),
        allow_abbrev=True,
    )
    get_parser.add_argument(
        "--start",
        help="The start of the date range for the desired data.",
        # format="yyyy-mm-dd",
    )
    get_parser.add_argument(
        "-e",
        "--end",
        help="The date to stop retrieving data for.",
        # format="yyyy-mm-dd",
    )

    return parser


def get_args() -> list[str]:
    """Retrieve CLI arguments."""
    return sys.argv[1:]


def main() -> int:
    """Execute the cds-helper CLI."""
    args_list = get_args()

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()

    parser = create_parser()

    if not args_list:
        parser.print_help()
        return 0

    try:
        if args_list:
            parser.parse_args(args_list)
    except SystemExit:
        log.debug("Unable to parse arguments", extra={"args_list": args_list})
        return 1

    return 0


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
