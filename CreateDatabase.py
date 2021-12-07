from pymongo import MongoClient
import certifi

try:
    client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
    db=client["office"]
    coll=db["workers"]
    query=[{'_id': '24607', 'Name': 'Willie Basque', 'Department': 'Hardware', 'Post': 'Laboratory Technician', 'City': 'Delhi', 'Salary': 86976.0, 'Mobile': '8611219140', 'E-Mail': 'WillieBasque1927@outlook.com'},
{'_id': '24408', 'Name': 'David Mccarthy', 'Department': 'Software', 'Post': 'Sales Executive', 'City': 'Barlin', 'Salary': 43584.0, 'Mobile': '6747600022', 'E-Mail': 'DavidMccarthy1694@outlook.com'},
{'_id': '24996', 'Name': 'Vivian Hankinson', 'Department': 'Support', 'Post': 'Manufacturing Director', 'City': 'Chennai', 'Salary': 32926.0, 'Mobile': '4669391866', 'E-Mail': 'VivianHankinson1032@outlook.com'},
{'_id': '24691', 'Name': 'Georgia Farmer', 'Department': 'Software', 'Post': 'Human Resources', 'City': 'Mosco', 'Salary': 64122.0, 'Mobile': '8302711308', 'E-Mail': 'GeorgiaFarmer220@gmail.com'},
{'_id': '24741', 'Name': 'Willie Fahnestock', 'Department': 'Research & Development', 'Post': 'Sales Representative', 'City': 'Chennai', 'Salary': 88609.0, 'Mobile': '9655869785', 'E-Mail': 'WillieFahnestock771@gmail.com'},{'_id': '24739', 'Name': 'Kathleen Stribling', 'Department': 'Sales', 'Post': 'Research Director', 'City': 'Mumbai', 'Salary': 15485.0, 'Mobile': '6330915920', 'E-Mail': 'KathleenStribling239@outlook.com'},
{'_id': '24915', 'Name': 'Phillip Maxfield', 'Department': 'Sales', 'Post': 'Healthcare Representative', 'City': 'Haidrabad', 'Salary': 70036.0, 'Mobile': '6521908470', 'E-Mail': 'PhillipMaxfield1776@outlook.com'}
]

    coll.insert_many(query)
    print("document added successfuy")

except:
    print("failed to add documents")