# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
#name. phone, title, email, department

namelist = ["Kevin C. Chang", "Donna Coleman", "Sarita Adve", "Molly Flesner", "Vikram Adve", "Tarek F. Abdelzaher", "Brian P. Bailey", "Matthew Caesar", "Jeff Erickson", "Margaret M. Fleck", "Philip Brighten Godfrey", "María Jesús Garzarán", "Carl A. Gunter", "Indy Clay", "Indranil Gupta", "Karrie G. Karahalios", "Jiawei Han", "Shanna M. DeSouza", "Tierra McCurry", "Laxmikant V. Kale", "Alexandra Kolla", "Aditya Parameswaran", "Manoj M. Prabhakaran", "Luke Olson", "Rob A. Rutenbar", "Karen Stahl", "Tierra Reed", "Saurabh Sinha", "Dan Roth"]
deps = ["Computer Science", "Electrical and Computer Engineering", "Statistics"]

phone_re = re.compile(r'''
    (\D?)
    (\d{3})     # area code is 3 digits (e.g. '800')
    (\D{,6}?)         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    (\D{,6}?)         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D{,6}?         # optional separator
    #(\d*)       # extension is optional and can be any number of digits
            # end of string
    ''', re.VERBOSE)


re1='((?:[a-z][a-z]+))'	# Word 1
re2='(((\\s+)?)'	# White Space 1
re3='((\\(|-|\\[))'	# Any Single Character 1
re4='((?:[a-z][a-z]+))'	# Word 2
re5='((\\)|-|\\]))'	# Any Single Character 2
re6='(( ?))'	# Any Single Character 3
re7='((?:[a-z][a-z1-9(.)]+))'	# Word 3
re8='(( )'	# Any Single Character 4
re9='((\\(|-|\\[))'	# Any Single Character 5
re10='(dot)'	# Word 4
re11='((\\)|-|\\]))'	# Any Single Character 6
re12='( )'	# White Space 2
re13='((edu|com))'	# Word 5
re14 = '|@)'
re15 = '|.)'
email_pattern = re.compile(re1+((re2+re3+re4+re5+re6+re14))+re7+((re8+re9+re10+re11+re12+re15))+re13,re.IGNORECASE|re.DOTALL)
#email_pattern = re.compile(r"([-a-zA-Z0-9._]+)([-a-zA-Z0-9]+)(@|[\D\Dat\D\D])([-a-zA-Z0-9_]+)(.com|.edu|([[(]dot[)]])com|([[(]dot[)]])edu)")
    


###############longest common subsequence, to check whose email it is##############
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result
################################################################################


url2= ["https://wiki.cites.illinois.edu/wiki/display/kevinchang/Kevin+C.+Chang", "https://cs.illinois.edu/directory/profile/kcchang", "http://luthuli.cs.uiuc.edu/~daf/contact.html", "http://rsim.cs.illinois.edu/~sadve/contact.html", "http://web.engr.illinois.edu/~vadve/Contact_Info.html","http://web.engr.illinois.edu/~zaher/", "http://orchid.cs.illinois.edu/people/bailey/index.html", "http://web.engr.illinois.edu/~caesar/", "http://jeffe.cs.illinois.edu/address.html", "http://mfleck.cs.illinois.edu/", "http://pbg.cs.illinois.edu/", "http://polaris.cs.uiuc.edu/~garzaran/", "http://web.engr.illinois.edu/~cgunter/?page_id=8", "http://indy.cs.illinois.edu/", "http://hanj.cs.illinois.edu/", "http://social.cs.uiuc.edu/people/kkarahal.html", "http://charm.cs.illinois.edu/~kale/", "http://akolla.cs.illinois.edu/", "http://lukeo.cs.illinois.edu/", "http://web.engr.illinois.edu/~adityagp/", "http://mmp.cs.illinois.edu/", "http://l2r.cs.illinois.edu/contact.html", "http://rutenbar.cs.illinois.edu/contact/", "http://www.sinhalab.net/sinha-s-home"]
info = []
emails = []
phone_pos = []
for url in url2:
    ok = []
    email = []
    phonpos = []
    #url = "http://rsim.cs.illinois.edu/~sadve/contact.html"
    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup(data)
    for tag in soup.find_all('script'):
        tag.replaceWith('')
    for tag in soup.find_all('style'):
        tag.replaceWith('')
    soup = soup.find('body')                 #why didn't I do this before
    m = soup.get_text()
    m = m.encode('utf-8')
    m = m.split("\n")
    m[:] = [x.decode('utf-8').strip() for x in m if x.decode('utf-8').strip() != '']
    m[:] = [x.replace('&nbsp', '') for x in m]
    #print m
    #divs = soup.findAll('body') 
    for count in range(len(m)):
                x = m[count]
                if x != None:
                    for l in phone_re.findall(x):
                            num = l[0]+l[1]+l[2]+l[3]+l[4]+l[5]
                            if ("(" in num and ")" in num) or ("(" not in num and ")" not in num):
                                ok.append(num)
                                phonpos.append((count, x.find(num)))
                    j = email_pattern.findall(x)
                    if len(j)>0:
                        for l in j:
                            combine =l[0]+l[1]+l[11]+l[12]+l[21]
                            email.append(combine)
    info.append(ok)
    emails.append(email)
    phone_pos.append(phonpos) 
fil = open("C:\Users\Harshit Agarwal\Desktop\contacts.txt", 'w')  
fil.write(str(info))
fil.write("\n")
fil.write(str(emails))

electronic_mails = []
for abc in emails:
    electronic_mails.append(abc)
#electronic_mails.append(list(ee) for ee in emails)
#electronic_mails = list(electronic_mails)
phone_dict = {}
for i in info:
    for j in i:
        if phone_dict.has_key(j):
            phone_dict[j]+=1
        else:
            phone_dict[j] = 1

final_phones = []
final_pos = []
for a in range(len(info)):
    final_phones.append([])
    final_pos.append([])
    for b in range(len(info[a])):
        if phone_dict[info[a][b]]==1:
            final_phones[-1].append(info[a][b])
            final_pos[-1].append(phone_pos[a][b])
fil.write("\n")
fil.write(str(final_phones))
fil.write("\n")

#print final_phones
#print info
#print final_pos
#print info
#print emails

#################################################################################
it = 0 #iterator
result_list = []
for url in url2:
    result_list.append([])
    thisphone = final_phones[it]
    alsothisphone = thisphone
    thispos = final_pos[it]
    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup(data)
    for tag in soup.find_all('script'):
        tag.replaceWith('')
    for tag in soup.find_all('style'):
        tag.replaceWith('')
    soup = soup.find('body')                 #why didn't I do this before
    m = soup.get_text()
    m = m.encode('utf-8')
    m = m.split("\n")
    m[:] = [x.decode('utf-8').strip() for x in m if x.decode('utf-8').strip() != '']
    m[:] = [x.replace('&nbsp', '') for x in m]
    
    namefound = []
    thisurl = (url, [])
    for name in namelist:
        if (name.decode('utf-8') in ' '.join(m)):
            namefound.append(name)
            thisurl[1].append((name, [], [], []))
    for kk in emails[it]:
        for count in range(len(namefound)):
            if ' ' in kk:
                jjj = kk
                kk = kk.split(' ')
                kk = kk[0]
            elif '@' in kk:
                jjj=kk
                kk = kk.split('@')
                kk = kk[0]
            lencheck = lcs(kk, namefound[count].lower())
            if len(lencheck)>=5:
                print jjj
                #emails[it].remove(kk)
                thisurl[1][count][1].append(jjj)
                #thisurl[1][count][1] = list(set(thisurl[1][count][1]))
                break
    for counter in range(len(thisphone)):
        aaaaa=0
        line = thispos[counter][0]
        notmatched = []
        position = thispos[counter][1]
        for count in range(len(namefound)):
            namehere = namefound[count]
            if namehere.decode('utf-8') in m[line]:
                if m[line].find(namehere.decode('utf-8'))<position:
                    thisurl[1][count][2].append(thisphone[counter])
                    alsothisphone.remove(thisphone[counter])
    try:
        thisurl[1][0][2].append(alsothisphone)
    except:
        okdidntwork = 0
    result_list.append(thisurl)
    it+=1
print result_list
                



##################################################################################################################
both = []
twocount = 0
ecount = 0
pcount = 0
nocount = 0
i=0
for mm in url2:
    if len(emails[i])>0 and len(info[i])>0:
        both.append(mm + "   " + "BOTH")
        twocount+=1
    elif len(emails[i])>0:
        both.append(mm + "   " + "ONLY EMAIL")
        ecount+=1
    elif len(info[i])>0:
        both.append(mm + "   " + "ONLY PHONE")
        pcount+=1
    else:
        both.append(mm + "   " + "NONE")
        nocount+=1
    i+=1
fil.write("\n")
fil.write(str(both))
fil.close

print "both found in "+str(twocount)

print "email only found in "+str(ecount)

print "phone only found in "+str(pcount)

print "neither found in "+str(nocount)