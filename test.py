from datetime import datetime

import pymongo

db_main = pymongo.MongoClient('mongodb+srv://police-department:1234567890@police-department-jezpl.mongodb.net/test?retryWrites=true&w=majority')
db = db_main["users"]
db = db["users"]

settings = db_main['settings']
settings = settings['settings']

applic = db_main['applications']
applic = applic['applications']
# query = settings.find({'123'})
# value = '123'
# for x in query:
#     print(x.values())
#     values = x.values()
#     if value in values:
#         print('ok')

# d = {'1': '2', '3':'4'}
# print(d.keys())
# if '2' in d.values():
#     print(list(d.values()).index('2'))
#     print('ok')

# query = settings.find({})
# print(query)
# for x in query:
#     print(x)


# query = {'level':'worker1', 'history': ['1234']}
# # query = applic.find({'username':'test1'})
#
# newvalues = { "$set": { "history":  ['1234','2345']} }
#
# applic.update_one(query, newvalues)
# for x in applic.find():
#  print(x)

# your_data_app = applic.find_one({'_id': '5ea319c59a95aee1fd50f591'})
# print(your_data_app)
# for x in your_data_app:
#     print(x)

# applic.update_one({'_id': "ObjectId('5ea319c59a95aee1fd50f591')"}, { "$set": { "history": ['1'], 'check': '1' }})
# for x in applic.find():
#     print(x)

# data_app = applic.find({'level': 'worker1', 'check': None})
#
# data_app1 = applic.find({'level': 'worker1', 'check': '1234'})
#
# for x in data_app:
#     print(x)
#
# for y in data_app1:
#     print(y)\

# data_app = applic.find({})
# new = list()
# your = list()
# for x in data_app:
#     if x


print(list('123456789sfdffggh'))