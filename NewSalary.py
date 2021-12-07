from pymongo import MongoClient
import certifi


client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["office"]
coll=db["workers"]
dic={}
sl={}

try:
    id=int(input("Enter id : "))
    dic["_id"]=id
    doc=coll.find_one(dic)
    if doc:
        sal=float(input("Enter a New Salary : "))
        sl["Salary"]=sal
        coll.update_one(dic,{"$set":sl})
        print("New Salary Is Successfuly updated")
        print(coll.find_one(dic))

    else:
        print("Document Not Find")
        



except:
    print("invalid input")