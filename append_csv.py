import csv
def append(filepath,name,email):
    with open(filepath,"a") as csvfile:
        writer=csv.DictWriter(csvfile)
        writer.writerow({
            "name":name,
            "email":email,
        })