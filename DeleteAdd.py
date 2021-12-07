from pymongo import MongoClient
import certifi


client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["office"]
coll=db["workers"]
coll2=db["exworkers"]



try:
    id =int(input('Enter Employee id : '))
    
    dic = coll.find_one({"_id":id})

    if dic:
        coll2.insert_one(dic)
        coll.delete_one({"_id":id})
        print('Employee is removed from Workers collection')

    else:
        print('Employee not found')
        
except:
    print("invalid input")