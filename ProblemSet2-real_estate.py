# Your co-worker at DataScienster comes up to you and asks for your help. 
# She would like to buy a 1-bedroom apartment in the city, and she has a preferred area she likes.
# She has managed to collect some data for the listings (asking price and sold) in that zip code (see your data set).
# Her questions are: 
# 1. What's the average price for a 1 BD place?
# 2. What's the average price for a 2 BD place?
# 3. (bonus question) Is Esprit Park cheaper than other places in the neighborhood for a 1 BD?

# Step 1: create your lists of prices: 1 list for 1 BD, 1 list for 2 BD 
# hint 1: see lists in Python
# your code goes here:
x = [1755,1900,1850,2000,2500,2700]
y = [3000,2750,2900,2100,3300,3500]

# Step 2: calculate the sum of prices in each list (see sum in Python)
# hint 2: see sum() in Python
# your code goes here:
sumx = sum(x)
sumy = sum(y)
    
# Step 3: calculate the length of each list
# hint 3: see len(), see float() in Python
# your code goes here:
lx = len(x)
ly = len(y)

# Step 4: calculate the average for each list, print it out
# hint 4: look at numpy.mean function, np.array().mean()
# your code goes here
avgx = sumx/lx
avgy = sumy/ly

print("Average price for a one-bedroom in San Francisco is %.2f" % avgx)
print("Average price for a two-bedroom in San Francisco is %.2f" % avgy)
