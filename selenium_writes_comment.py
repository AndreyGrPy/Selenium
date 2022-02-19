import time
from selenium import webdriver
#from instagr_data import instagramm_phone, instagramm_password  (creating and import file in which the butet will be stored log and passwd)
from selenium.webdriver.common.keys import Keys

"""options"""
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0)"
                     " Gecko/20100101 Firefox/97.0")#substitution useragent

#headless mode(view without opening a browser window)
# options.headless = True

#disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")


def get_data():
    try:
        driver = webdriver.Chrome("./chromedriver", options=options)
        url = "https://www.instagram.com/"
        driver.get(url)
        driver.implicitly_wait(5)
#login entry
        login_right = driver.find_element_by_name("username")
        login_right.send_keys(instagramm_phone)
        time.sleep(3)
#password entry
        passwd_right = driver.find_element_by_name("password")
        passwd_right.send_keys(instagramm_password)
        time.sleep(3)
#click to login
        passwd_right.send_keys(Keys.ENTER)
        time.sleep(6)
#search html elements
        click = driver.find_elements_by_class_name("sqdOP")[1].click()
        time.sleep(4)

        click2 = driver.find_elements_by_class_name("aOOlW")[1].click()
        time.sleep(6)

        comment = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div/div[3]/div/div/section[1]/span[2]/button/div[2]")
        comment.click()
        time.sleep(6)

        wright_comment = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    get_data()