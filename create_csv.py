import csv
fieldnames=["name","email"]
with open("file1.csv","w") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {
            "name":"azeez",
            "email":"abdulazeez2197@gmail.com",
        }
    )