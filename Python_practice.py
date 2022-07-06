county = ["Arapahoe", "Denver", "Tahoe"]
print(county)
print(county[0])
len(county)
print(county[:2])
county.append("El Paso")
print(county)
print(county[2:])
print(county.pop(3))
print(county)
county[2]="Davenport"
print(county)
print(county[:2])
print(county[1:2])
counties_tuple = ("D.C.", "Room", "House")
len(counties_tuple)
print(counties_tuple[:-1])
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
print(counties_dict)
len(counties_dict)
counties_dict.get("Denver")
voting_data = [{"county":"Arapahoe","registered_voters": 422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
voting_data
voting_data.append({"county":"El Paso","registered_voters":461149})
voting_data.pop(0)
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data
voting_data.pop(-1)
voting_data.pop(0)
voting_data.insert(0,{'county': 'Jefferson', 'registered_voters': 432438})
voting_data.pop(-1)
voting_data.insert(1,{'county': 'El Paso', 'registered_voters': 461149})
voting_data
voting_data.pop(-1)
voting_data.append({"county":"Arapahoe","registered_voters": 422829})
voting_data
import datetime
now = datetime.datetime.now()
print("The time right now is ", now)
