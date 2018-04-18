from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pymongo
from pymongo import MongoClient
 
def learning () :
	print("aprendendo");

def getAtigosCLT(url) :
	driver = webdriver.Chrome()
	driver.get(url)
	try:
		WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.entry-title.td-module-title a')))
		elements = driver.find_elements(By.CSS_SELECTOR, '.entry-title.td-module-title a')
		for i in elements :
			getAtigosCLT(i.get_attribute("href"));
		print("found list")
	except:	
		try:
			WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.td-post-content')))
			content = driver.find_element(By.CSS_SELECTOR, '.td-post-content')
			title = driver.find_element(By.CSS_SELECTOR, '.entry-title')
			insert(content.text, title.text)
		except:
			print("Achou nada")
	driver.close()


def insert(artigo, title) :
    client = MongoClient('mongodb://localhost:27017/Harvey')
    db = client['Harvey']
    collection = db['Artigos']
    res = collection.insert({"artigo" : artigo,"title" : title } );

lista = [];
artigos = [];

url = "https://www.direitocom.com/clt-comentada"
#url = "https://www.direitocom.com/clt-comentada/titulo-i-introducao/artigo-1o-2"

getAtigosCLT(url)
