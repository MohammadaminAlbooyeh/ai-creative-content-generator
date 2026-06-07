from datetime import datetime, timedelta


class AnalyticsService:
    def __init__(self):
        self.events = []

    async def track(self, event_type: str, metadata: dict = None):
        self.events.append({
            "type": event_type,
            "metadata": metadata or {},
            "timestamp": datetime.now(),
        })

    async def get_generation_count(self, since: timedelta = timedelta(days=7)) -> int:
        cutoff = datetime.now() - since
        return sum(1 for e in self.events if e["type"] == "generation" and e["timestamp"] > cutoff)

    async def get_popular_content_types(self) -> dict:
        counts = {}
        for e in self.events:
            if e["type"] == "generation":
                ct = e["metadata"].get("content_type", "unknown")
                counts[ct] = counts.get(ct, 0) + 1
        return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
