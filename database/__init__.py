import aiosqlite, os

class Database:
    def __init__(self, *, connection: aiosqlite.Connection) -> None:
        self.conn = connection