from faker import Faker
from pymongo import MongoClient
from bson.objectid import ObjectId

import datetime
class MongoDB:
    def __init__(self, mongo_db_url: str, mongo_db_name: str):
        self.client = MongoClient(mongo_db_url)
        self.url = mongo_db_url
        self.db = self.client[mongo_db_name]
        self.faker = Faker()

    def create_attachment(self):
        attachment = {
            "file_name": self.faker.word(),
            "file_size": self.faker.word(),
            "file_type": self.faker.word(),
            "date_of_upload": datetime.datetime.now(),
            "uploader_id": ObjectId(),
            "task_id": ObjectId()
        }
        self.db.Attachments.insert_one(attachment)
        
    def create_user_notification(self):
        notification = {
            "notification_text": self.faker.text(),
            "creation_date": datetime.datetime.now(),
            "addresser_id": ObjectId()
        }
        self.db.UserNotifications.insert_one(notification)

    def create_task_comment(self):
        comment = {
            "comment": self.faker.text(),
            "date_of_creation": datetime.datetime.now(),
            "user_id": ObjectId(),
            "task_id": ObjectId()
        }
        self.db.TaskComments.insert_one(comment)

    def remove_attachment(self):
        attachment = self.db.Attachments.find_one()
        if attachment:
            self.db.Attachments.delete_one({"_id": attachment["_id"]})

    def read_attachment(self):
        return self.db.Attachments.find_one()

    def update_attachment(self):
        attachment = self.db.Attachments.find_one()
        if attachment:
            updated = {
                "date_of_upload": datetime.datetime.now(),
                "uploader_id": ObjectId()
            }
            self.db.Attachments.update_one(
                {"_id": attachment["_id"]},
                {"$set": updated}
            )

    def crud_m(self):
        self.create_attachment()
        self.read_attachment()
        self.update_attachment()
        self.remove_attachment()
