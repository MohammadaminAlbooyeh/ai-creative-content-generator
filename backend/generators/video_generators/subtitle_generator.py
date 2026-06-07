class SubtitleGenerator:
    def __init__(self):
        self.max_line_length = 42
        self.max_duration = 5

    async def generate(self, text: str, language: str = "en"):
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            if len(" ".join(current_line)) > self.max_line_length:
                lines.append(" ".join(current_line[:-1]))
                current_line = [word]

        if current_line:
            lines.append(" ".join(current_line))

        subtitles = []
        for i, line in enumerate(lines):
            start = i * self.max_duration
            end = (i + 1) * self.max_duration
            subtitles.append({
                "index": i + 1,
                "start": start,
                "end": end,
                "text": line,
            })

        return subtitles
