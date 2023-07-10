import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('freepikproject-25c3cc5c26db.json', scope)


client = gspread.authorize(credentials)


sheet = client.open("url_database").sheet1


url = sheet.acell('A1').value

# Print the URL
print(url)

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get(url)

# Find and click the download button
#time.sleep(10)
download_button = driver.find_element(By.ID, 'download-file')
download_button.click()
download2_button = driver.find_element(By.CLASS_NAME, 'download-button')
download2_button.click()
time.sleep(10)

# Close the browser
# driver.quit()