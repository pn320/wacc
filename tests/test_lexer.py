from wacc.lexer import get_tokens_from_string


def test_get_tokens_from_string():
    assert get_tokens_from_string("") == []
