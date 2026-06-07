class PodcastTemplate:
    def __init__(self):
        self.name = "podcast"

    def render(self, title: str, intro: str, segments: list[dict], outro: str, guest: str = None) -> str:
        seg_text = "\n\n".join([f"Segment {i+1}: {s['topic']}\n{s['content']}" for i, s in enumerate(segments)])
        guest_text = f"Guest: {guest}\n\n" if guest else ""
        return f"Title: {title}\n\n{guest_text}INTRO:\n{intro}\n\n{seg_text}\n\nOUTRO:\n{outro}"
