import requests

url = "https://en.wikipedia.org/wiki/Special:Random" #gets a random wikipedia article

def html(url):
    r = requests.get(url)
    return r.text #gets html from website

for i in range(4): #can change to another number for more/fewer html files
    f = open(str(i)+".html", 'w') #creates file
    f.write(html(url)) #writes html to file
    f.close() #close file