from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'Driver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#driver.get('https://google.com')
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://onlineonly.christies.com/s/latin-american-art-online/lots/2004")
#driver.get("https://www.sothebys.com/en/buy/auction/2021/contemporary-prints-multiples?locale=en")
print(driver.page_source)
# h1 = driver.find_element_by_name('h1')
# h1 = driver.find_element_by_class_name('someclass')
# h1 = driver.find_element_by_xpath('//h1')
# h1 = driver.find_element_by_id('greatID')
# all_links = driver.find_elements_by_tag_name('a')
# <input type="hidden" id="custId" name="custId" value="">
#driver.get("https://news.ycombinator.com/login")

# login = driver.find_element_by_xpath("//input").send_keys(USERNAME)
# password = driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
# submit = driver.find_element_by_xpath("//input[@value='login']").click()
driver.quit()