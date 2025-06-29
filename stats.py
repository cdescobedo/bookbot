from typing import Any


def get_word_count(input: str) -> int:
    return len(input.split())


def get_char_count(input: str) -> dict[str, int]:
    char_count = {}
    for char in input:
        char = char.lower()
        if char in [" ", "\r", "\n", "\t"]:
            continue

        if char_count.get(char, ""):
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_dictionary(input: dict[str, int]) -> list[dict[str, Any]]:
    result = []
    for k, v in input.items():
        result.append({"char": k, "num": v})

    result.sort(reverse=True, key=lambda x: x["num"])
    return result
