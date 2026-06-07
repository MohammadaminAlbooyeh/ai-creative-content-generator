class StyleTransfer:
    def __init__(self):
        self.styles = [
            "oil painting",
            "watercolor",
            "sketch",
            "digital art",
            "pixel art",
            "3D render",
            "impressionist",
            "abstract",
        ]

    async def apply(self, image_url: str, target_style: str):
        prompt = f"Transform the image at {image_url} into {target_style} style"
        return prompt
