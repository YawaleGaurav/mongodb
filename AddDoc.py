from pymongo import MongoClient
import certifi


client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["office"]
coll=db["workers"]
doc={}

try:
    id=int(input("Enter Employee ID : "))
    nm=input("Enter  Employee Name  :  ")
    dept=input("Enter Department    :  ")
    post=input("Enter Employee Post : ")
    ct=input("Enter City            :  ")
    sal=float(input("Enter Salary   : "))
    mob=int(input("Enter Mobile No. : "))
    eml=input("Enter E-Mail Id        : ")

    doc["_id"]=id
    doc["Name"]=nm
    doc["Department"]=dept
    doc["Post"]=post
    doc["City"]=ct
    doc["Salary"]=sal
    doc["Mobile"]=mob
    doc["E-Mail"]=eml

    coll.insert_one(doc)
    print("Document Successfuly Added")

except:
    print("Failed to add")
    
    




