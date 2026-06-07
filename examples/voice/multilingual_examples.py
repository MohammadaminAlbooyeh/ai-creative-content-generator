"""Example: Generate speech in multiple languages."""


def run_examples():
    from backend.generators.voice_generators.accent_selector import AccentSelector

    selector = AccentSelector()
    accents = selector.list_accents()
    for accent in accents:
        code = selector.get_language_code(accent)
        print(f"{accent}: {code}")
