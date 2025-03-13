#StudentMainProj.py<---------------Main Program
from StudentMenu import menu
from StudentAdd import Savestuddata
from StudentViews import getallrecords, getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                Savestuddata()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4:
                deleterecord()
            case 5:
                updaterecord()
            case 6:
                searchrecord()
            case 7:
                print("Thx for using this App")
                break
            case _:
                print("Ur Selection of Operation wrong-Try again")
    except ValueError:
        print("Don't Enter alnums,strs and symbols for Choice--try again")