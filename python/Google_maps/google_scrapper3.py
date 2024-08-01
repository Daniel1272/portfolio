import undetected_chromedriver as uc
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import random
from database import add_to_database

# Gmail credentials for login
GMAIL = 'gmail adress'
PASSWORD = 'password'

# Chrome options to enhance stealth and handle browser configuration
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")

# Initialize the undetected Chrome driver with the configured options
driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()

# Navigate to the Google Maps search page
driver.get('https://www.google.com/maps/search/logistics/@52.2665071,-2.3194654,268770m/data=!3m1!1e3?entry=ttu')
driver.implicitly_wait(5)

# Click on the sign-in button
driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb').click()
driver.implicitly_wait(5)

# Enter the Gmail address and submit
driver.find_element(By.TAG_NAME, 'input').send_keys(GMAIL, Keys.RETURN)
time.sleep(5)

# Enter the password and submit
(driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div'
 '/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
 .send_keys(PASSWORD, Keys.RETURN))
time.sleep(5)

# Optional clicks for initial setup (uncomment if needed)
#driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div/button/span').click()
#driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div[2]/div[4]/div[1]/button/span').click()


def main_loop():
    # Find the first clickable element and click it
    element = driver.find_element(By.CLASS_NAME, 'hfpxzc')
    element.click()

    # Scroll down to load more elements
    for _ in range(1000):
        element.send_keys(Keys.DOWN * 4)

    # Find all elements matching the class name
    elements = driver.find_elements(By.CLASS_NAME, 'hfpxzc')
    for el in elements:
        try:
            # Scroll the element into view and click it
            driver.execute_script("arguments[0].scrollIntoView(true);", el)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", el)
            time.sleep(random.choice([1, 1.2, 1.3, 1.5, 1.7, 1.57, 1.89]))
            driver.implicitly_wait(5)

            # Parse the page source with BeautifulSoup
            soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
            res = soup.find_all('div', {'class': 'Io6YTe fontBodyMedium kR99db'})

            # Log if no results are found
            if not res:
                print("Could not find the expected div. Here is the page source:")
                print(soup.prettify())
                continue

            # Patterns for extracting phone number, address, and website
            phone_number_pattern = re.compile(r'\+?[\d\s]{10,16}')
            address_pattern = re.compile(r'(Unit\s?\d*\.?\d*,)? ?(\d*-?\d*)? \D+, [\w\s]+,? [\w\s]+')
            website_pattern = re.compile(r'\S{3,}(\.\w{2,})+')

            # Initialize variables to store extracted information
            phone_number = None
            address = None
            website = None

            # Extract information based on patterns
            for div in res:
                text = div.get_text()
                if not phone_number:
                    phone_number_match = phone_number_pattern.search(text)
                    if phone_number_match:
                        phone_number = phone_number_match.group()
                if not address:
                    address_match = address_pattern.search(text)
                    if address_match:
                        address = address_match.group()
                if not website:
                    website_match = website_pattern.search(text)
                    if website_match:
                        website = website_match.group()

            # Add extracted information to the database
            add_to_database(phone_number, address, website)



        except Exception as e:
            print(f"Error: {e}")

        finally:
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

# Run the main loop
main_loop()
