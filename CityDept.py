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
        ct=input("Enter a New City : ")
        sl["City"]=ct
        dept=input("Enter New Department : ")
        sl["Department"]=dept
        coll.update_one(dic,{"$set":sl})
        print("New City & New Department Is Successfuly updated")
        print(coll.find_one(dic))

    else:
        print("Document Not Find")
        



except:
    print("invalid input")