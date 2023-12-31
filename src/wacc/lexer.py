from dataclasses import dataclass
from enum import Enum, auto
import re

import structlog


logger = structlog.get_logger(__name__)


class TokenType(Enum):
    # Keywords
    Begin = auto()
    End = auto()
    Exit = auto()

    # Whitespace
    Whitespace = auto()

    # Literals
    IntLiteral = auto()


@dataclass
class Token:
    token_type: TokenType
    value: str
    line: int = 0
    column: int = 0


def _create_token(token, token_type: TokenType):
    return Token(token_type, token)


def get_tokens_from_string(source: str) -> list[Token]:
    tokens: list[Token] = []
    # this is an undocumented feature of the re module and is not type checked
    scanner = re.Scanner(  # type: ignore
        [
            (
                r"(?P<_begin>\bbegin\b)",
                lambda _, token: _create_token(token, token_type=TokenType.Begin),
            ),
            (
                r"(?P<_end>\bend\b)",
                lambda _, token: _create_token(token, TokenType.End),
            ),
            (
                r"(?P<_exit>\bexit\b)",
                lambda _, token: _create_token(token, TokenType.Exit),
            ),
            (
                r"(?P<_num>(-)?\d+)",
                lambda _, token: _create_token(token, TokenType.IntLiteral),
            ),
            (r"(?P<_ws>\s+)", None),
        ]
    )

    for token, match in scanner.scan(source):
        logger.debug(f"@{token=} @{match=}")

    return tokens
