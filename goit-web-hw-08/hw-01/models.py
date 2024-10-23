from mongoengine import *

connect(
    db="web16",
    host="mongodb+srv://userweb216:567234@cluster0.zy7kn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
# mongodb+srv://userweb216:<db_password>@cluster0.zy7kn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

class Contact(Document):
    email_sent = BooleanField(default=False)
    full_name = StringField(max_length=150)
    email = StringField(max_length=150)
    country = StringField(max_length= 50)
