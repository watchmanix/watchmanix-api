from collections import OrderedDict

from aiosqlite import Cursor


async def get_raw_sql(get_query, *args, **kwargs):
    sql, params = "", ()
    try:
        sql, params = await get_query(*args, **kwargs)
    except ValueError:
        sql = await get_query()
    return sql, params


async def get_many_result(cursor: Cursor):
    if cursor.description:
        columns: list[str] = [element[0] for element in cursor.description]
        fetch = await cursor.fetchall()
        return [OrderedDict(zip(columns, row)) for row in fetch]
    return None


async def get_one_result(cursor: Cursor):
    if cursor.description:
        columns: list[str] = [element[0] for element in cursor.description]
        fetch = await cursor.fetchone()
        fetch = fetch if fetch else []
        return OrderedDict(zip(columns, fetch))
    return None
