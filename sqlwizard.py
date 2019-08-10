import sqlite3


class SQLWizard():
    # from collections import OrderedDict
    #
    # a = OrderedDict([
    #     ("1", "a"),
    #     ("2", "b"),
    #     ("3", "c")
    # ])

    def __init__(self, filename):
        self.open_db(filename)


    def open_db(self, filename):
        self.db_conn = sqlite3.connect(filename)
        self.db_cursor = self.db_conn.cursor()


    def close_db(self):
        self.db_conn.close()


    def create_table(self, table_name, table_data):
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS {} (
                {}
            )
        """.format(
            table_name,
            ", ".join(["{} {}".format(key, value) for key, value in table_data.items()])
        ))
        self.db_conn.commit()


    def delete_table(self, table_name):
        self.db_cursor.execute("""
            DROP TABLE IF EXISTS {}
        """.format(
            table_name
        ))
        self.db_conn.commit()


    def insert(self, table_name, table_data):
        self.db_cursor.execute("""
            INSERT INTO {}
            ({})
            VALUES({})
        """.format(
            table_name,
            ", ".join([key for key in table_data.keys()]),
            ", ".join(["'{}'".format(value) for value in table_data.values()])
        ))
        self.db_conn.commit()


    def delete(self, table_name, where_data=False):
        self.db_cursor.execute("""
            DELETE FROM {}
            WHERE {}
        """.format(
            table_name,
            where_data
        ))
        self.db_conn.commit()


    def update(self, table_name, table_data, where_data):
        self.db_cursor.execute("""
            UPDATE {}
            SET {}
            WHERE {}
        """.format(
            table_name,
            ", ".join(["{} = '{}'".format(key, value) for key, value in table_data.items()]),
            where_data
        ))
        self.db_conn.commit()


    def select(self, columns, table_name, where_data=False):
        if where_data:
            self.db_cursor.execute("""
                SELECT {}
                FROM {}
                WHERE {}
            """.format(
                columns,
                table_name,
                where_data
            ))
        else:
            self.db_cursor.execute("""
                SELECT {}
                FROM {}
            """.format(
                columns,
                table_name
            ))
        self.db_conn.commit()

        return self.db_cursor.fetchall()
