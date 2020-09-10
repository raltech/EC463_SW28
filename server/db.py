import sqlite3


def getConnection() -> sqlite3.Connection:
    return sqlite3.connect('sensors.db')


def addSensor(conn: sqlite3.Connection, user_id: str, sensor_type: str, name: str):
    if sensor_type != "temperature" and sensor_type != "humidity":
        raise Exception('sensor_type must be in {"temperature", "humidity"}')

    createTableStatement = """
    CREATE TABLE IF NOT EXISTS sensors (user_id text, sensor_type text, name text);
    """
    insertStatement = "INSERT INTO sensors(user_id, sensor_type, name) VALUES (?,?,?);"

    c = conn.cursor()
    c.execute(createTableStatement)
    c.execute(insertStatement, (user_id, sensor_type, name))
    conn.commit()
    c.close()


def getSensors(conn: sqlite3.Connection, user_id: str):
    getSensorsStatement = """
    SELECT sensor_type, name FROM sensors WHERE user_id=?;
    """

    c = conn.cursor()
    c.execute(getSensorsStatement, (user_id,))
    rows = c.fetchall()
    conn.commit()
    c.close()
    return rows
