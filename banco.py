
from tinydb import TinyDB
db = TinyDB('banco.json')

db.remove(doc_ids=[1])
