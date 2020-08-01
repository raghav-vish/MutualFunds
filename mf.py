import requests
import bs4
import lxml
from openpyxl import *
from datetime import *

book = load_workbook('MFDetails.xlsx')
funds = book["Fundwise Details"]
row_count = funds.max_row - 4

res=requests.get("http://mf6.herokuapp.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')
amt = soup.find_all("div")
for i in range(1, len(amt)+1):
	print(amt[i-1].text)
	funds['K'+str(i+3)]=amt[i-1].text

funds['K1'] = 'Updated on '+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

book.save('MFDetails.xlsx')