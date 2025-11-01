def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_character_counts(text: str) -> dict[str, int]:
    characters_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def get_sorted_character_counts(character_counts: dict[str, int]) -> list[dict[str, int]]:
    sorted_counts = []
    for char, count in character_counts.items():
        sorted_counts.append({char: count})
    sorted_counts.sort(key=lambda x: list(x.values())[0], reverse=True)
    return sorted_counts