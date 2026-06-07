class QualityService:
    def __init__(self):
        self.min_content_length = 50
        self.max_content_length = 10000

    async def check(self, content: str) -> dict:
        issues = []
        if len(content) < self.min_content_length:
            issues.append("Content is too short")
        if len(content) > self.max_content_length:
            issues.append("Content exceeds maximum length")
        return {
            "passed": len(issues) == 0,
            "issues": issues,
            "length": len(content),
        }
