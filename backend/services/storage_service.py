from pathlib import Path


class StorageService:
    def __init__(self, base_path: str = "data/processed"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    async def save(self, filename: str, content: bytes) -> str:
        file_path = self.base_path / filename
        file_path.write_bytes(content)
        return str(file_path)

    async def read(self, filename: str) -> bytes:
        file_path = self.base_path / filename
        return file_path.read_bytes()

    async def delete(self, filename: str) -> bool:
        file_path = self.base_path / filename
        if file_path.exists():
            file_path.unlink()
            return True
        return False
