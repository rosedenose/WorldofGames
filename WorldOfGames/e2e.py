from selenium import webdriver
import sys

def test_scores_service(url):
    my_driver = webdriver.Chrome("chromedriver.exe")
    my_driver.get(f"{url}")
    actual = my_driver.find_element(by="id", value="score").text

    if int(actual) in range(1000):
        return True
    else:
        return False

def main_function():
    result = test_scores_service("http://127.0.0.1:4444")
    if result == True:
        return sys.exit(0)
    elif result == False:
        return sys.exit(-1)