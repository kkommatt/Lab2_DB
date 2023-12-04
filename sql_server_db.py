import random
from datetime import datetime

import pyodbc
from bson import ObjectId
from faker import Faker


class SqlServerDB:
    def __init__(self, connection_string):
        self.conn = pyodbc.connect(connection_string)
        self.faker = Faker()

    def create_attachment(self):
        attachment = {
            "file_name": self.faker.word(),
            "file_size": random.randint(1, 100),
            "file_type": self.faker.word(),
            "date_of_upload": datetime.now(),
            "uploader_id": random.randint(1, 100),
            "task_id": random.randint(1, 100)
        }
        with self.conn.cursor() as cur:
            sql_query = """
                INSERT INTO Attachments (file_name, file_size, file_type, date_of_upload, uploader_id, 
                                      task_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """

            cur.execute(sql_query, (
                attachment["file_name"], attachment["file_size"], attachment["file_type"],
                attachment["date_of_upload"], attachment["uploader_id"], attachment["task_id"]
            ))
            self.conn.commit()

    def update_attachment(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id FROM Attachments;")
            result = cur.fetchone()
            attachment_id = result[0] if result else None
        if attachment_id is None:
            return 0

        updated_data = {
            "date_of_upload": datetime.now(),
            "uploader_id": random.randint(1, 100)
        }

        with self.conn.cursor() as cur:
            query = "UPDATE Attachments SET "
            query += ", ".join([f"{key} = ?" for key in updated_data])
            query += " WHERE id = ?"

            values = list(updated_data.values()) + [attachment_id]

            cur.execute(query, values)
            self.conn.commit()
            return cur.rowcount

    def delete_attachment(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT TOP 1 id FROM Attachments;")
            result = cur.fetchone()
            attachment_id = result[0] if result else None
        if attachment_id is None:
            return 0

        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM Attachments WHERE id = ?", (attachment_id))
            self.conn.commit()
            return cur.rowcount

    def read_attachment(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT TOP 1 id FROM Attachments;")
            result = cur.fetchone()
            attachment_id = result[0] if result else None
            if attachment_id is None:
                return None

            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM Attachments WHERE id = ?", (attachment_id,))
                return cur.fetchone()

    def crud_sql(self):
        self.create_attachment()
        self.read_attachment()
        self.update_attachment()
        self.delete_attachment()