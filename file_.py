# file = open("student_records.txt", mode='w')
# file.write("001 mariam 75\n")
# file.write("002 david 75\n")
# file.write("003 sultan 75\n")
# file.write("004 torin 75\n")
# file.close()

# with open("record2.txt", mode='w') as file:
#     file.write("005 hyelnati 75\n")
#     file.write("006 segun 75\n")
#     file.write("007 esther 75\n")


with open("record2.txt", mode='r') as records:
    for record in records:
        num, name, score = record.split()
        print(f"{num:<10} {name: <10} {score: >10}")








