import pickle
def getallrecords():
    try:
        with open("STU.data","rb") as fp:
            print("_"*50)
            print("Student Details")
            print("_"*50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("_"*50)
                    break
    except FileNotFoundError:
        print("File does not Exist")
def getrecord():


    try:
        with open("STU.data","rb") as fp:
            records=[]
            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                          break
                    #get student number from kbd to get other details from file
        try:
                sno=int(input("Enter Student Number to get other Details:"))
                found=False
                for record in records:
                    if(sno==record[0]):
                        found=True
                        break
                if(found):
                    print("\tStudent Number:{}".format(record[0]))
                    print("\tStudent Name:{}".format(record[1]))
                    print("\tStudent Marks:{}".format(record[2]))
                else:
                    print("Student Record Does not Exist")
        except ValueError:
            print("Dont't enter Alnums, strs and symbols for sno--try again")
    except FileNotFoundError:
        print("File Does not exist")

