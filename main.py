import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_termin(tor, termin):
    os.popen(tor)

    proxy = 'socks5://localhost:9050'
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument('window-position=2900,0')

    driver = webdriver.Chrome(options=options)

    driver.get(termin)

    try:
        buchbar = driver.find_element_by_xpath('//td[@class="buchbar"]')
        buchbar.click()
        time.sleep(10000)
    except NoSuchElementException:
        nextpage = driver.find_element_by_xpath('//a[@title="nächster Monat ab (01-09-2021)"]')
        nextpage.click()
        try:
            buchbar = driver.find_element_by_xpath('//td[@class="buchbar"]')
            buchbar.click()
            time.sleep(10000)
        except NoSuchElementException:
            driver.close()
            driver.quit()
    finally:
        os.system('taskkill /im tor.exe /f')


if __name__ == '__main__':
    tor_path = r'C:\Users\---\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
    termin_path = input('Enter Termin URL: ')

    while True:
        get_termin(tor_path, termin_path)
