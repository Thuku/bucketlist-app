from flask import Flask
from models.user import User
from models.bucketlist import BucketList
from models.activity import Activity

app = Flask(__name__, instance_relative_config=True)
app.secret_key = "theseahamthatyouwillnevergettounderstand"


user_instance = User()
bucket = BucketList()
bucket_item = Activity()

from app import views

app.config.from_object('config')
