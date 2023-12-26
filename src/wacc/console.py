# entry point for the program
import sys


def print_help() -> None:
    print(
        "Usage: wacc [--source-file=<path>] [--output-file=<path>]"
        " [-v | --version] [--help]"
    )
    exit(0)


def get_file_name_from_path(path: str) -> str:
    """Returns the file name from the given path by returning the
    last bit of the string after the final '/' character in the path."""
    return path.strip().split("/")[-1]


def parse_args(args: list[str]) -> None:
    """Parses the command line arguments and runs the compiler
    with the appropriate flags as specified by the user."""
    ...


def main() -> None:
    """
    The entry point for the program. Captures the command line arguments
    and runs the compiler if the correct arguments are given else
    prints the help message.
    """
    args: list[str] = sys.argv[1:]
    match args:
        case []:
            print_help()
        case _:
            parse_args(args)
