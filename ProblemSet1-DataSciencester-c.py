from collections import defaultdict

# This was a data science project I worked on from PyLadies Meetup Group

# Data set 1
users = [
  {"id":0, "name":"Hero"},
  {"id":1, "name":"Dunn"},
  {"id":2, "name":"Sue"},
  {"id":3, "name":"Chi"},
  {"id":4, "name":"Thor"},
  {"id":5, "name":"Clive"},
  {"id":6, "name":"Hicks"},
  {"id":7, "name":"Devin"},
  {"id":8, "name":"Kate"},
  {"id":9, "name":"Klein"}
]

# Data set 2
interests = [
  (0, "Hadoop"), (0, "Big Data"), (0, "Spark"),
  (1, "Python"), (1, "MongoDB"), (1, "scikit-learn"),
  (2, "numpy"), (2, "R"), (2, "Python"), (2, "pandas"),
  (3, "statistics"), (3, "probability"), (3, "regression"),
  (4, "machine learning"), (4, "regression"), (4, "decision trees"),
  (5, "R"), (5, "Python"), (5, "statistics"),
  (6, "probability"), (6, "mathematics"), (6, "machine learning"),
  (7, "machine learning"), (7, "scikit-learn"), (7, "neural networks"),
  (8, "Big Data"), (8, "artificial intelligence"), (8, "hadoop"),
  (9, "Java"), (9, "MapReduce"), (9, "Big Data")]

# Step 1: build a function that finds users with a certain interest
# (hint: it's better to use an index, as in key value pairs (data structures: dictionary, defaultdict))
# Step 2: iterate over the user's interests: for each interest, iterate over the other users with that interest
# Step 3: keep count of how many times we see each user
# Step 4: Print out each interest and all the users that have this interest in common 
# (optional) Use a counter to find out which interest comes up most often. 
# (optional) Print out the list of interests in descending order of frequency.
# your solution:

#create a dictionary of user id : user name from users list
userkeys = []
uservalues = []
user_dict = {}

for i in users:
    userkeys.append(i["id"])

for j in users:
    uservalues.append(j["name"])

user_dict = dict(zip(userkeys,uservalues))

print(user_dict)

#write a short function to get user name associated with user ID
def GetUser(num):
    name = ""
    if num in user_dict:
        name = user_dict[num]
        return name
    else:
        print("No records found for user Id %d." % num)


#create a defaultdict with each interest : list of users
def by_interest(dataset):
    by_interest = defaultdict(list)
    for user, interest in interests:
        by_interest[interest].append(user)

    return by_interest

### tallying the number of interested users per topic ###
count = 0
maxnum = 0
tally_keys = []

#calling by_interest function by passing it the data set "interests"
tally = by_interest(interests)
print(tally)

print("\n")
print("Topic of interest: Number of Users interested\n")
for item in tally:
    #create a list of interest topics as keys
    tally_keys.append(item)
    #count the length of the list in tally values
    count = len(tally[item])
    print(item +": "+ str(count))



print("\n")
print ("Topic of interest : User Names\n")

#A function to print out usernames without the list syntax
def makeString(alist):
    output = ""
    output = str(alist)
    output = output.replace("[","")
    output = output.replace("]","")
    output = output.replace("'","")
    return output

#output user names per topic of interest:
names = ""
for item in tally:
    userlist = []
    usernames = []
    #put the user ids into a list in order to iterate over it
    userlist.extend(tally[item])
    #call the GetUser function for each  user id in the list
    for n in userlist:
        usernames.append(GetUser(n))
        #calls makeString() to convert username list into a string for printing
        names = makeString(usernames)
        
    print (item + ": " + names)




    


    


    




    










    
