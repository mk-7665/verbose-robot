#orig gets user's input on the initial base sequence
#uses a for loop to convert the string into an integer list
orig = input("Enter the base sequence: ")
orig = orig.split(",")
my_list = []

for s in range(len(orig)):
    my_list.append(int(orig[s]))
    
new_list = []
y = len(my_list)
n = int(input("Enter how many times: "))
mult = list(range(1,(n+1)))
#print(mult)

#iterate over the range of how many times, from 1 to n
k = 0

for j in mult:
    #print(j)
    #iterate over my_list for each element in my_list
    for i in my_list:
        new_list.append(i+y)
        print(new_list[k])
        k = k+1
    print('***************')
    my_list = new_list
    new_list = []
    k = 0

#be sure to assign the new list back to x, so that the next loop starts with the new values
#be sure to set the new list back to null, otherwise it will still contain the values of the last iteration
    
    


