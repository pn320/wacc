import argparse
from wacc import console
import pytest


@pytest.mark.parametrize(
    "path, expected",
    [
        ("", ""),
        ("test.wacc", "test.wacc"),
        ("programs/test.wacc", "test.wacc"),
        ("programs/basic/exit/exitBasic.wacc", "exitBasic.wacc"),
    ],
)
def test_file_from_path(path: str, expected: str):
    assert console.get_file_name_from_path(path) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            ["test.rlx"],
            argparse.Namespace(
                source="test.rlx", output_file=None, o1=False, o2=False, ast_only=False
            ),
        ),
        (
            ["test.rlx", "--output-file=test.s"],
            argparse.Namespace(
                source="test.rlx",
                output_file="test.s",
                o1=False,
                o2=False,
                ast_only=False,
            ),
        ),
    ],
)
def test_command_line_parser(args: list[str], expected: argparse.Namespace):
    assert console.parse_args(args) == expected
