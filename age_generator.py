#my fist python code
import datetime
name=input("what is your name ")
print(" welcome "+name+" to your first code ")
year= (input(" what year were you born "))
current_year= datetime.datetime.now().year
age= str(current_year-int(year))
print(" not many "+age+" year olds make it this far ")
