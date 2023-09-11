import datetime

class SerialNumber:
    def __init__(self, ubication: str, content: str, search_time: float) -> None:
        self.ubication = ubication
        self.content = content
        self.search_time = search_time

    def __str__(self) -> str:
        return f"{self.ubication}\t{self.content}\n"