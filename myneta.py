from webscraping import common, download, xpath
from lxml import html
import requests
import json


def scrape(url,filename):
	page = requests.get(url)
	raw = page.text
	tree = html.fromstring(raw)
	
	names = tree.xpath('//table[3]/tr/td/a/text()')
	sid = tree.xpath('//table[3]/tr/td[1]/text()')
	cons = tree.xpath('//table[3]/tr/td[3]/text()')
	party = tree.xpath('//table[3]/tr/td[4]/text()')
	link = tree.xpath('//table[3]/tr/td/a/@href')
	
	neta_list = []
	email=''
	phone=''

	print names;
	
	for i in range(0,len(sid)):
		page_u = requests.get(link[2*i+1])
		raw_u = page_u.text
		tree_u = html.fromstring(raw_u)
		try:
			addr = tree_u.xpath('//div[@class="grid_2 alpha"][4]/text()')[1].strip()
		except IndexError:
			addr = ''
		try:
			email = tree_u.xpath('//div[@class="grid_2 alpha"][5]/text()')[0]
		except IndexError:
			email = ''
		try:
			phone = tree_u.xpath('//div[@class="grid_2 alpha"][6]/text()')[0]
		except IndexError:
			phone = ''
		neta = {'id':sid[i], 'name':names[i], 'constituency':cons[i], 'party':party[i], 'addr':addr, 'email': email, 'phone':phone}
		neta_list.append(neta)
	
	#print neta_list
	with open(filename, 'w') as outfile:
		json.dump(neta_list,outfile)
	print filename+" Done!"

#scrape('http://www.myneta.info/ls2014/index.php?action=show_winners&sort=default','India')
#scrape('http://www.myneta.info/andhra2014/index.php?action=show_winners&sort=default','AndhraPradesh')
#scrape('http://www.myneta.info/arunachal2014/index.php?action=show_winners&sort=default','ArunachalPradesh')
#scrape('http://www.myneta.info/assam2011/index.php?action=show_winners&sort=default','Assam')
#scrape('http://www.myneta.info/bih2010/index.php?action=show_winners&sort=default','Bihar')
#scrape('http://www.myneta.info/chattisgarh2013/index.php?action=show_winners&sort=default','Chattishgarh')
scrape('http://www.myneta.info/delhi2013/index.php?action=show_winners&sort=default','Delhi')
#scrape('http://www.myneta.info/goa2012/index.php?action=show_winners&sort=default','Goa')
#scrape('http://www.myneta.info/gujarat2012/index.php?action=show_winners&sort=default','Gujarat')
#scrape('http://www.myneta.info/ha2009/index.php?action=show_winners&sort=default','Haryana')
#scrape('http://www.myneta.info/hp2012/index.php?action=show_winners&sort=default','HimachalPradesh')
#scrape('http://www.myneta.info/jk2008/index.php?action=show_winners&sort=default','Jammu&Kashmir')
#scrape('http://www.myneta.info/jarka09/index.php?action=show_winners&sort=default','Jharkhand')
#scrape('http://www.myneta.info/karnataka2013/index.php?action=show_winners&sort=default','Karnataka')
#scrape('http://www.myneta.info/kerala2011/index.php?action=show_winners&sort=default','Kerala')
#scrape('http://www.myneta.info/mp2013/index.php?action=show_winners&sort=default','MadhyaPradesh')
#scrape('http://www.myneta.info/mh2009/index.php?action=show_winners&sort=default','Maharashtra')
#scrape('http://www.myneta.info/manipur2012/index.php?action=show_winners&sort=default','Manipur')
#scrape('http://www.myneta.info/meghalaya2013/index.php?action=show_winners&sort=default','Meghalaya')
#scrape('http://www.myneta.info/mizoram2013/index.php?action=show_winners&sort=default','Mizoram')
#scrape('http://www.myneta.info/nagaland2013/index.php?action=show_winners&sort=default','Nagaland')
#scrape('http://www.myneta.info/odisha2014/index.php?action=show_winners&sort=default','Odisha')
#scrape('http://www.myneta.info/puducherry2011/index.php?action=show_winners&sort=default','Puducherry')
#scrape('http://www.myneta.info/pb2012/index.php?action=show_winners&sort=default','Punjab')
#scrape('http://www.myneta.info/rajasthan2013/index.php?action=show_winners&sort=default','Rajasthan')
#scrape('http://www.myneta.info/sikkim2014/index.php?action=show_winners&sort=default','Sikkim')
#scrape('http://www.myneta.info/tamilnadu2011/index.php?action=show_winners&sort=default','TamilNadu')
#scrape('http://www.myneta.info/tripura2013/index.php?action=show_winners&sort=default','Tripura')
#scrape('http://www.myneta.info/utt2012/index.php?action=show_winners&sort=default','Uttarakhand')
#scrape('http://www.myneta.info/up2012/index.php?action=show_winners&sort=default','UttarPradesh')
#scrape('http://www.myneta.info/westbengal2011/index.php?action=show_winners&sort=default','WestBengal')
