# entry point for the program

import sys
import structlog
import argparse
from wacc import __version__

logger = structlog.get_logger(__name__)


def get_file_name_from_path(path: str) -> str:
    """Returns the file name from the given path by returning the
    last bit of the string after the final '/' character in the path."""
    return path.strip().split("/")[-1]


def parse_args(args: list[str]) -> argparse.ArgumentParser:
    """Creates the parser for the command line arguments."""
    parser = argparse.ArgumentParser(prog="wacc")
    parser.add_argument(
        "--version", "-v", action="version", version="%(prog)s " + __version__
    )
    parser.add_argument(
        "source", metavar="source", type=str, help="the source file to compile"
    )
    parser.add_argument(
        "--output-file",
        metavar="",
        type=str,
        help="the output file for the compiled program",
    )
    parser.add_argument("-o1", action="store_true", help="enable basic optimisations")
    parser.add_argument(
        "-o2", action="store_true", help="enable advanced optimisations"
    )
    parser.add_argument(
        "--ast-only",
        action="store_true",
        help="only output the ast of the program in the most readable format possible",
    )
    return parser.parse_args(args)


def main(argv: list[str] | None = None) -> None:
    """
    The entry point for the program. Captures the command line arguments
    and runs the compiler with the supplied arguments.
    """
    # this is to ensure test args are not passed to the parser
    # unless they are explicitly passed
    _ = parse_args(sys.argv[1:] if argv is None else argv)
