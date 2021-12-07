from pymongo import MongoClient
import certifi


client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["office"]
coll=db["workers"]


try:
    sl =float(input('Enter Employee Salary : '))
    
    doc = coll.find({"Salary":{"$gt":sl}})
    for item in doc:
        print(item)
    
except:
    print("No Document Found")