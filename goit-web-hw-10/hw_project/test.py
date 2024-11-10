import os
import django
from pymongo import MongoClient
import pprint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()
from quotes.models import Quote, Tag, Author, Automobile #noqa
from quotes.models import  Automobile
client = MongoClient("mongodb://localhost")
db = client.hw
authors =db.authors.find()


author = db.authors.find_one({'fullname':'Albert Einstein'})

quotes = db.quotes.find()
print(author)

# for quote in quotes:
#     tags =[]
#     for tag in quote['tags']:
#         t, *_ = Tag.objects.get_or_create(name=tag)
#         tags.append(t)

#     a = Author.objects.get(fullname=author['fullname'])
#     q = Quote.objects.create(
#         quote=quote['quote'],
#         author=a 
#     )
# print(tags)
    # for tag in tags:
    #     q.tags.add(tag)
# try:
#     obj = Automobile.objects.get(producer="Fiat", type="van", model_name="Doblo")
# except Automobile.DoesNotExist:
#     obj = Automobile(producer="Fiat", type="van", model_name="Doblo")
#     obj.save()
