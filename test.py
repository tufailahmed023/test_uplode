import pymongo

client = pymongo.MongoClient("mongodb+srv://tufail:shaikhahmed@cluster0.q6hm0vv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
database = client['myinfo']
collections=database['shaikh']
collections1 = database['dpkt']
record=collections.find()
for i in record :
    print(i)
print('-------'*25)
print('-------'*25)
data=collections.find({'companyName':"iNeuron"})
for i in data:
    print(i)
print('-------'*25)
print('-------'*25)
data1=collections.find({'courseOffered':{'$gt':"E"}})
for i in data1:
    print(i)

