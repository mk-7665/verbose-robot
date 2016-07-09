import os

count = 0
directory = input("Input a sub-directory: ")

print("Files with zero byte sizes are:")
#use os.walk to search through the current working directory
    
for root, dirs, files in os.walk(directory):
    for file in files:
        fullpath = os.path.join(root,file)
        #use os.path.join to get the filenames of each file
        filename = os.path.basename(fullpath)
        filesize = (os.path.getsize(fullpath))
        #use os.path.getsize to find the size of each file
        if filesize == 0:
            print("{0} {1}".format(filename,filesize))
            count = count + 1
            #increment count if it is a zero byte size file
                
print("Total number of zero byte size files: % d" % count)
      
        


