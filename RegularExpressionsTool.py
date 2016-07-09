import re, sys
import urllib.request

def get_images(url):
    imgpat = re.compile(r'<img [^>]+>', re.IGNORECASE)
    #look for string that start with "<img "
    #match everything except the first set of ">" it sees
    try:
        file = urllib.request.urlopen(url)
    except IOError:
        sys.stderr.write("Couldn't connect to %s " % url)
        sys.exit(1)

    imgnames = []
    newlist = []

    lines = file.readlines()
    #read all the lines of the url file
        
    for line in lines:
        string = str(line)
        #convert each line of bytes to string
        imgnames = imgpat.findall(string)
        #apply image pattern search
        newlist.extend(imgnames)
        #combine old list with new list of string elements that match imgpat
    
    file.close()

    return newlist
#return a list of image names found


url = 'http://www.nytimes.com/'
images = get_images(url)

for image in images:
    print(image)
print("Webpage has {0} images".format(len(images)))
    







