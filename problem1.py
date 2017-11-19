import urllib2 #for fetching the URLs
from bs4 import BeautifulSoup #Beautiful Soup is a python library for pulling data out of HTML and XML
import csv #For dealing with the CSV files and data

def check_redirection(url): 
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req, timeout=3)
    redirected = resp.geturl() != url # redirected will be a boolean True/False
    return redirected

regions = ["american","arabic","australian","christian","english","french","german","indian"] #creating an array of regions

genders = ["boy","girl"] #array of genders

letters = list("abcdefghijklmnopqrstuvwxyz") #list of letters

url = "https://www.babynamesdirect.com/baby-names" #the URL to be searched

with open("names.csv", "wb") as csvfile: #looping into the names.csv
    spamwriter = csv.writer(csvfile, delimiter=',') #writing data into names.csv using delimeter
    spamwriter.writerow(["name","gender"])

def get_names(url,gender): #function to get the names by reading the HTML of the page
    page = urllib2.urlopen(url) #contains whole webpage of the URL
    soup = BeautifulSoup(page) #stores whole format of the page
    all_li=soup.find_all('li', class_='ntr') #storing all lists with HTML class ntr
    for i in all_li: #looping into the HTML to get the data and writing it into names.csv
        if(i.dl):
            if(i.dl.dt):
                if(i.dl.dt.b):
                    if(i.dl.dt.b.a):
                        with open("names.csv", "a") as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=',') #writing into names.csv
                            spamwriter.writerow([i.dl.dt.b.text, gender])

for region in regions: #loop to search for different regions stored in the array
    url_now = url + "/" + region #changed URL
    for gender in genders: #Loop gender and add gender to the URL for different cases
        url_now_2 = url_now + "/" + gender #changed URL
        for letter in letters: #again adding letters to the URL
            url_now_1 = url_now_2 + "/" + letter #changed URL
            get_names(url_now_1, gender) #getting names for that changed URL
            print url_now_1 #displaying that URL
            const = 2
            url_number = url_now_1 + "/" + str(const) #adding number to the URL
            while(not(check_redirection(url_number))): #check whether the URL is redirected or not
                get_names(url_number, gender) #retrieving names from that URL
                print url_number #displaying URL
                const = const + 1
                url_number = url_now_1 + "/" + str(const) #changing the URL