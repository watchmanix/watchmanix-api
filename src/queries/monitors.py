async def get_list_monitors():
    return "SELECT * FROM monitors"


async def insert_monitor(name: str):
    return "INSERT INTO monitors (name) VALUES (?)", (name,)


async def get_monitor_by_id(id: int):
    return "SELECT * FROM monitors WHERE id = ?", (id,)


async def update_monitor_by_id(id: int):
    return "UPDATE monitors SET name = 'some name' WHERE id = ?", (id,)


async def delete_monitor_by_id(id: int):
    return "DELETE FROM monitors WHERE id = ?", (id,)
