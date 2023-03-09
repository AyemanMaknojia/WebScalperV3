#from org.openqa.selenium import By
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys
#initialize chrome driver
driver = webdriver.Chrome();
#open the amazon item link (the second arguement)
driver.get(sys.argv[2])
#get the page source of the amazon item
html_source = driver.page_source
i=0
#keep going through the while loop until i is greater than a value (first arguement)
while i<int(sys.argv[1]):
    #if an add to cart button is present in the page source then run the code inside if statement
    if ("submit.add-to-cart" in html_source):
        #automates a click to the add to cart button
        driver.find_element(By.ID, "add-to-cart-button").click()
        #sleep for 3 seconds, then quit the driver
        time.sleep(2)
        driver.quit()
    else:
        time.sleep(1);
        #driver will refresh until there is an add to cart button, or until it reaches the end of the while loop.
        driver.refresh()
        i+=1
driver.quit()



