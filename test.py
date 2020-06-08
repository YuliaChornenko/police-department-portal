from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
import pymongo
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome import Random
from Cryptodome.Cipher import AES
# import chardet
#
from bson.objectid import ObjectId
db_main = pymongo.MongoClient('mongodb+srv://police-department:1234567890@police-department-jezpl.mongodb.net/test?retryWrites=true&w=majority')
db = db_main["users"]
db = db["users"]
settings = db_main['settings']
settings = settings['settings']
applic = db_main['applications']
applic = applic['applications']
id = '5ea73753e07792e19826cc1c'

n = b'\x95\xd8\x9a\xaa,S\xdc`\xc7\x10W\x99>\xbc\x0c\xb4doth'

m = n.decode('utf-8')
print(m)