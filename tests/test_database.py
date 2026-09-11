from database.database_manager import DatabaseManager

def test_database_connection():
    db = DatabaseManager()

    connection = db.connect()

    assert connection is not None

    connection.close()