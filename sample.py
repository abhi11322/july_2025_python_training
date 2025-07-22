
from datetime import datetime
curr = datetime.now()
filename=str(curr).replace(":","_")

user_input = input("enter some text : ")

with open(filename +".txt","w") as file:
    file.write(user_input)

print("done succesfully")
