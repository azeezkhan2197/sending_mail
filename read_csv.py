import csv
def read(filepath,number):
    with open(filepath,"r") as csvfile:
        reader=csv.DictReader(csvfile)
        i=0
        return_values={}
        for row in reader:
            i=i+1
            if(i==number):
                return_values["name"]=row["name"]
                return_values["email"]=row["email"]
            return return_values