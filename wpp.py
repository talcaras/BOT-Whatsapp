from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

def qrok():
    print('QR CODE OK')
    grupo = driver.find_element_by_xpath('inserir aqui o xpath da conversa')
    grupo.click()
    inputtext = driver.find_element_by_xpath('colocar pra digitar')
    inputtext.click()
    inputtext.send_keys('testando')
    botao = driver.find_element_by_xpath('enviar mensagem')
    botao.click()

qrcode = input("QRCODE OK: ?")
if qrcode == "sim" or qrcode == "s":
    qrok()


    