from collections.abc import Callable

import aiosqlite

from src.config import get_settings

from .utils import get_many_result, get_one_result, get_raw_sql


class Database:
    def __init__(self, uri: str):
        self.uri = uri

    async def connect(self):
        self._connection = await aiosqlite.connect(self.uri)
        self._cursor = await self._connection.cursor()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    async def commit(self):
        await self.connection.commit()

    async def close(self, commit=True):
        if commit:
            await self.commit()
        await self.connection.close()

    async def fetchall(self, get_query: Callable, *args, **kwargs):
        await self.__execute_sql(get_query, *args, **kwargs)
        return await get_many_result(self.cursor)

    async def fetchone(self, get_query: Callable, *args, **kwargs):
        await self.__execute_sql(get_query, *args, **kwargs)
        return await get_one_result(self.cursor)

    async def insert_and_return_id(self, get_query: Callable, *args, **kwargs):
        await self.__execute_sql(get_query, *args, **kwargs)
        await self.commit()
        return self.cursor.lastrowid

    async def execute(self, get_query: Callable, *args, **kwargs):
        await self.__execute_sql(get_query, *args, **kwargs)
        await self.commit()

    async def __execute_sql(self, get_query, *args, **kwargs):
        sql, params = await get_raw_sql(get_query, *args, **kwargs)
        await self.cursor.execute(sql, params)
        return


settings = get_settings()


db = Database(settings.secrets.db.URI)
