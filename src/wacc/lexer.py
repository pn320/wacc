from dataclasses import dataclass


@dataclass
class Token:
    token_type: str
    value: str
    line: int
    column: int


def get_tokens_from_string(source: str) -> list[Token]:
    return []
