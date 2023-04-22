import aiosqlite
import asyncio
import os


db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'db.db')


async def init_db():
    async with aiosqlite.connect(db_path) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS Users(username TEXT UNIQUE, status INT, times INT DEFAULT 0);''')
        await db.commit()


async def insert_db(username, status):
    async with aiosqlite.connect(db_path) as db:
        if status == 0:
            try:
                await db.execute('INSERT INTO Users(username, status) VALUES (?, ?);', (username, status))
                return True
            except:
                await db.execute('UPDATE Users SET status = 0, times = 1 WHERE username = ?;', (username, ))
                return False
        else:
            await db.execute('UPDATE Users SET status = ? WHERE username = ?;', (status, username))
        await db.commit()


async def get_statistics(i):
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute('SELECT COUNT(*) FROM Users WHERE status = ?;', (i,))
        count = await cursor.fetchone()
        cursor = await db.execute('SELECT username FROM Users WHERE status = ?;', (i,))
        usernames = await cursor.fetchall()
        return count, usernames

       
