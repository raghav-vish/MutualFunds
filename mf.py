import requests
import bs4
import lxml
from openpyxl import *
from datetime import *

book = load_workbook('MFDetails.xlsx')
funds = book["Fundwise Details"]
row_count = funds.max_row - 4


for i in range(1, row_count):
	url = funds.cell(row=i+3, column=7)
	res = requests.get(url.value)
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	amt = soup.find_all("span", class_="amt")[0].text[2:]
	funds['K'+str(i+3)]=amt

funds['K1'] = 'Updated on '+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

book.save('MFDetails.xlsx')