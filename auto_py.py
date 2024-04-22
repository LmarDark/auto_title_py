from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.implicitly_wait(1.0)

user = "XXXXXXXXXXXXXXX" # AQUI VOCÊ INSERE SEU USUÁRIO!
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(user);

password = "XXXXXXXXXXXXXXX" # AQUI VOCÊ INSERE SUA SENHA!
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(password);

driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()

driver.implicitly_wait(1.5)

sys.exit(0) 
