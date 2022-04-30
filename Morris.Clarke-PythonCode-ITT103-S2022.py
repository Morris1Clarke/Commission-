# Author: Morris Clarke
# Date Created: April 26, 2022
# Course: ITT103
# The purpose of this program is to test the logics of the pseudocode given and also to compute the commission rate of the given inputs.


print("************************************")
print("*           Welcome To             *")
print("*         JamEx Limited            *")
print("************************************")
 
    
while True:
    try:
        number = int(input("Please enter your Identification Number: \n"))
        class6  = int(input("Please Enter your class Category. Press 1, 2 or 3 for the class :\n "))
        saleNum = int(input("Please Enter your Sales Amount: \n"))
    except ValueError:
        print("You did not enter a valid input. Please try again!")
        continue   
    else:
        break
  
if class6 == 1:
  
    if saleNum <= 1000:     
        print("Your Commission is: ", 0.06 * saleNum)
elif 1000 < saleNum <= 2000: 
        print("Your Commission is: ", 0.07 * saleNum)
else:
        print("Your Commission is: ", 0.1 * saleNum)
    
#====================== CLASS 2 ===============================
        
if class6 == 2:
      if saleNum <= 1000:
        print("Your Commission is: ", 0.04 * saleNum)
else:
        print("Your Commission is: ", 0.06 * saleNum)

#====================== CLASS 3 ===============================
if class6 == 3:
        print("Your Commission is: ", 0.45 * saleNum)
elif class6 > 3:
        print("You did not enter a valid class reference!")
else:
        print("Press '1' to exit the Program")
one = int(input(""))
if one== 1:
        exit()

       
