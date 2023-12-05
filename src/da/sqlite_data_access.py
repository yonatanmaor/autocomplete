import sqlite3
import os

def get_connection():
    path = os.path.abspath('../../autocomplete_sqlite.db')
    if not os.path.exists(path):
        # running on docker
        path = os.path.abspath('/app/autocomplete_sqlite.db')
        if not os.path.exists(path):
            raise Exception(f"File {path} does not exist")
    connection = sqlite3.connect(path)
    return connection


def upsert_bulk_records(table_name, records: list[dict]):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        for record in records:
            columns = []
            values = []
            for key, value in record.items():
                columns.append(key)
                values.append(value)

            query = f"""INSERT OR REPLACE INTO {table_name} ({", ".join(columns)})
                        VALUES ({', '.join(['?' for _ in values])})"""

            cursor.execute(query, list(values))

        conn.commit()

    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()


def truncate_table(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()


def execute_query(query, params):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()
