import pickle
from VerifyDuplicateRecord import verify
class InvalidNameError(Exception):pass
class ZeroLengthError(BaseException):pass
class SpaceNameError(Exception):pass
#code for validation of Name
def validation(name):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
        words=name.split()
        res=True
        for word in words:
            if (not word.isalpha()):
                 res=False
                 break
            if (res):
                 return name
            else:
                raise InvalidNameError
def Savestuddata():
    with open("STU.data","ab") as fp:
        try: #read the student data from the kbd
            print("_____________________")
            sno=int(input("Enter Student Number:"))
            sname=validation(input("Enter Student Name:"))
            marks=float(input("Enter Student Marks:"))
            print("_____________________")
            #create an empty list for placing student vals
            lst=[]
            lst.append(sno)
            lst.append(sname)
            lst.append(marks)
            #save lst data to student.pickle file
            pickle.dump(lst,fp)
            print("Student record inserted")
            print("____________________________")
        except ValueError:
            print("Don't Enter alnums,strs and symbols for sno and marks")
        except InvalidNameError:
            print("Invalid Name--try again")
        except ZeroLengthError:
            print("Try to enter Your Name ")
        except SpaceNameError:
            print("Don't enter space for ur Name---try again")

