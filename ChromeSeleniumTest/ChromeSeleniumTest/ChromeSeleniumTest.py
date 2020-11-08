from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.bestbuy.ca/en-ca/product/toshiba-55-4k-uhd-hdr-led-smart-tv-55lf621c21-fire-tv-edition-only-at-best-buy/14422159')
addToCartButton = browser.find_element_by_xpath('//*[@id="test"]/button')
addToCartButton.click()

time.sleep(10)
goToCartButton = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div/div[4]/div[2]/div/a[1]')
goToCartButton.click()

time.sleep(5)
checkoutButton = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a')
checkoutButton.click()

time.sleep(2)
guestCheckoutButton = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div[2]/div/div[2]/a/span')
guestCheckoutButton.click()


time.sleep(7)
emailBox = browser.find_element_by_xpath('//*[@id="email"]')
emailBox.send_keys('whoisbricksy@gmail.com')

fNameBox = browser.find_element_by_xpath('//*[@id="firstName"]')
fNameBox.send_keys('Mankirat')

lNameBox = browser.find_element_by_xpath('//*[@id="lastName"]')
lNameBox.send_keys('Sarwara')

addressBox = browser.find_element_by_xpath('//*[@id="addressLine"]')
addressBox.send_keys('452 Rue Spring Garden')

cityBox = browser.find_element_by_xpath('//*[@id="city"]')
cityBox.send_keys('Montreal')

phoneBox = browser.find_element_by_xpath('//*[@id="phone"]')
phoneBox.send_keys('5147951728')

continueBox = browser.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button/span')
continueBox.click()

time.sleep(7)
cardNumberBox = browser.find_element_by_xpath('//*[@id="shownCardNumber"]')
cardNumberBox.send_keys('1111222233334444')

expMonthBox = browser.find_element_by_xpath('//*[@id="expirationMonth"]')
expMonthBox.send_keys('03')

expMonthBox = browser.find_element_by_xpath('//*[@id="expirationYear"]')
expMonthBox.send_keys('2027')

cvvBox = browser.find_element_by_xpath('//*[@id="cvv"]')
cvvBox.send_keys('123')

continueAgainBox = browser.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button/span')
continueAgainBox.click()