from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.headless = True

gecko_driver_path = "/usr/local/bin/geckodriver"
service = Service(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://forms.gle/WT68aV5UnPajeoSc8")

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))

print(driver.title)

time.sleep(5)

def fill_field(xpath, value):
    try:
        field = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", field)
        ActionChains(driver).move_to_element(field).click().perform()
        field.clear()
        field.send_keys(value)
    except Exception as e:
        print(f"Error finding or filling field '{xpath}': {e}")

fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input", "Safuan P Anvar")
fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input", "9895989268")
fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input", "safuananvar@gmail.com")
fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea", "123 Main St, Springfield")
fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input", "590533")

try:
    month_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input")))
    driver.execute_script("arguments[0].scrollIntoView(true);", month_field)
    month_field.click()
    month_field.clear()
    month_field.send_keys("01")

    day_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/input")))
    driver.execute_script("arguments[0].scrollIntoView(true);", day_field)
    day_field.click()
    day_field.clear()
    day_field.send_keys("01")

    year_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[5]/div/div[2]/div[1]/div/div[1]/input")))
    driver.execute_script("arguments[0].scrollIntoView(true);", year_field)
    year_field.click()
    year_field.clear()
    year_field.send_keys("2000")

except Exception as e:
    print(f"Error finding or filling Date of Birth fields: {e}")

fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input", "Male")
fill_field("/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input", "GNFPYC")

try:
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
except Exception as e:
    print(f"Error finding or clicking Submit button: {e}")

time.sleep(5)
driver.save_screenshot("/home/kali/Pictures/confirmation_page.png")
driver.quit()
