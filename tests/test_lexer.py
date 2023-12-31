import pytest
from wacc.lexer import Token, get_tokens_from_string


@pytest.mark.parametrize("source,expected", [("", []), ("begin\n  exit 0\nend", [])])
def test_get_tokens_from_string(source: str, expected: list[Token]):
    assert get_tokens_from_string(source) == expected
