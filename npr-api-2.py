#this script gets the latest science story from NPR
from urllib.request import urlopen
from urllib.request import quote
from json import loads, dumps
#this module prints out top two NPR stories in science


def url_sender(x,y):
        url = 'http://api.npr.org/query?apiKey=' 
        key = '[your-api-key-here]'
        url = url + key
        url += '&numResults='+ x + '&format=json&id='+ y + '&requiredAssets=image,text,audio'
        return url

#1007 is science

def json_response(request):
        #in 3, json module loads can only load strings. Besure to decode() json objects first
        response = urlopen(request).read()
        json_obj = loads(response.decode())
        return json_obj

def json_object(response):
        #in 3, json module dumps can only dump string objects. which loads() have already done above.
        f = open('output.json', 'w')
        f.write(dumps(response, indent=4))
        f.close()
        #outputs a .json file
        return f
        
def story_download(json_file, more):
        #checking for and printing out different elements in the story object
        for story in json_file['list']['story']:
                print ("TITLE: " + story['title']['$text'] + "\n")
                print ("DATE: " + story['storyDate']['$text'] + "\n")
                print ("TEASER: " + story['teaser']['$text'] + "\n")
                if 'byline' in story:
                    print ("BYLINE: " + story['byline'][0]['name']['$text'] + "\n")
                if 'show' in story:
                    print ("PROGRAM: " + story['show'][0]['program']['$text'] + "\n")
                print ("NPR URL: " + story['link'][0]['$text'] + "\n")
                print ("IMAGE: " + story['image'][0]['src'] + "\n")
                if 'caption' in story:
                    print ("IMAGE CAPTION: " + story['image'][0]['$text'] + "\n")
                if 'producer' in story:
                    print ("IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n")
                print ("MP3 AUDIO: " + story['audio'][0]['format']['mp3'][0]['$text'] + "\n")
                #print out the stories,one story at a time
                if more == 'y':
                        for item in json_file['list']:
                                for paragraph in story['textWithHtml']['paragraph']:
                                    print (paragraph['$text'] + "\n")
                elif more == 'n':
                        print("\n")
                else:
                        print("Cannot recognize input. Bye!")


num = 0
npr_id = 0


npr_id = input("Enter npr topic id: ")
num = input("Enter number of stories: ")
more = input("Print out transcript(s)? y or n ")

#pass input variables into the url_sender() function
query = url_sender(num,npr_id)

#pass query result to json_response() function
result = json_response(query)

#pass call result to json_object() function
file = json_object(result)

#pass call result to story_download() function to output story and mp3 link
stories = story_download(result,more)



        
        
