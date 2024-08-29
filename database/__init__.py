import aiosqlite, os

class Database:
    def __init__(self, *, connection: aiosqlite.Connection) -> None:
        self.conn = connection
    
    async def init_db(self) -> None:
        async with aiosqlite.connect(
            f"{os.path.realpath(os.path.dirname(__file__))}/database.db"
        ) as db:
            with open(
                f"{os.path.realpath(os.path.dirname(__file__))}/schema.sql"
            ) as file:
                await db.executescript(file.read())
            await db.commit()