from selenium import webdriver
from bs4 import BeautifulSoup
fil = open("C:/Users/Harshit Agarwal/Desktop/htmlselenium.txt", 'w')
path_to_chromedriver = 'C:/Users/Harshit Agarwal/Downloads/chromedriver/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://cs.illinois.edu/directory/faculty'
browser.get(url)
html = browser.page_source
browser.close()
#print html
fil.write(html.encode('utf-8'))
fil.close()
directory = {}
soup = BeautifulSoup(html)
lis = soup.findAll('div',attrs={'class':'content'})

for item in lis:
    lis2 = item.findAll('div',attrs={'class' : 'extDirectoryPerson'})
    #print len(lis2)
    for item2 in lis2:
        name = item2.find('div', attrs = {'class': 'extDirectoryName'})
        name = name.find('a')
        name = name.string
        title = item2.find('div', attrs = {'class': 'extDirectoryTitle'})
        title = title.string
        phone = item2.find('div', attrs = {'class': 'extDirectoryPhone'})
        try:
            phone = phone.string
        except:
            phone = "samplevalue"
        email = item2.find('div', attrs = {'class': 'extDirectoryEmail'})
        try:
            email = email.find('a')
            email = email.string
        except:
            email = "sample email"
        directory[name] = (title, phone,email)
#print directory
file2 = open("C:/Users/Harshit Agarwal/Desktop/allcontacts.txt", 'w')

for key, value in directory.iteritems():
    file2.write(key + "   :   " + str(value) + "\n")
file2.close()
    