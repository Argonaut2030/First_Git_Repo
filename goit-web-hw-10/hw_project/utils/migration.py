import os
import django
from pymongo import MongoClient
import pprint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author  #noqa
client = MongoClient("mongodb://localhost")
db = client.hw
authors =db.authors.find()


for author in authors:
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date = author['born_date'],
        born_location =  author['born_location'],
        description = author['description'],
        
    )

quotes = db.quotes.find()

for quote in quotes:
    tags =[]
    for tag in quote['tags']:
       t, *_= Tag.objects.get_or_create(name=tag)
       tags.append(t)
      

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id':quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a 
        )
        for tag in tags:
            q.tags.add(tag)


   

# {'_id': ObjectId('6727c247b8f3133dcd736a91'),
#  'author': ObjectId('6727c1d45b21c1383270e8ee'),
#  'quote': '“The world as we have created it is a process of our thinking. It '
#           'cannot be changed without changing our thinking.”',
#  'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
# {'_id': ObjectId('6727c247b8f3133dcd736a92'),
#  'author': ObjectId('6727c1d45b21c1383270e8f1'),
#  'quote': '“It is our choices, Harry, that show what we truly are, far more '
#           'than our abilities.”',
#  'tags': ['abilities', 'choices']}
