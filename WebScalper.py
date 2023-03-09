#from org.openqa.selenium import By
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys
driver = webdriver.Chrome();
driver.get(sys.argv[2])
html_source = driver.page_source
i=1
while i<int(sys.argv[1]):
    if ("submit.add-to-cart" in html_source):
     #automates a click to the add to cart button
     #driver.findElement(By.id("add-to-cart-button")).click()
     #driver.find_element(By.ID(str("add-to-cart-button"))).click()
        driver.find_element(By.ID, "add-to-cart-button").click()
    #sleep for 3 seconds, then quit the driver
    #time.sleep(500)
        time.sleep(3)
        driver.quit()
#break;
    else:
        time.sleep(1);
#driver will refresh until there is an add to cart button present, or the user manually switches it off.
        driver.refresh()
        i+=1
driver.quit()



