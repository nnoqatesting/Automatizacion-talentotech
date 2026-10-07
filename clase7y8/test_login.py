from selenium import webdriver
from selenium.webdriver.common.by import By # estamos importando seleccionar los elementos segun el id

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

input("Presiona ENTER para cerrar...")

driver.quit() 