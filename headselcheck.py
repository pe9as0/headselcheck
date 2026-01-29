import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Wzorce do wyszukiwania w kodzie strony
ONETRUST_PATTERNS = ("OneTrust", "cdn.cookielaw.org", "otSDKStub.js")
GTM_PATTERNS = ("https://www.googletagmanager.com/gtm.js", "GTM-", "SiteLocalContainer")

# Selenium conifg + chromium + webdriver
options = Options()
options.headless = True  # chromium w trybie headless

service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# dod.funkcjie
def check_cookies(cookies, cookie_names):
    for cookie_name in cookie_names:
        found = False
        for cookie in cookies:
            if cookie['name'] == cookie_name:
                print(f"Cookie '{cookie_name}' znaleziony: {cookie['value']}")
                found = True
                break
        if not found:
            print(f"Cookie '{cookie_name}' nie został znaleziony.")

def check_patterns_in_page_content(page_content, patterns, pattern_name):
    for pattern in patterns:
        if pattern in page_content:
            print(f"Wzorzec '{pattern}' związany z {pattern_name} znaleziony w zawartości strony.")
        else:
            print(f"Wzorzec '{pattern}' związany z {pattern_name} nie został znaleziony w zawartości strony.")

# Główna funkcja skryptu
def main(url):
    driver.get(url)
    time.sleep(4)  # Czekaj na załadowanie strony
    page_content = driver.page_source
    cookies = driver.get_cookies()
    
    # Przeszukanie ciasteczek
    check_cookies(cookies, ['OptanonConsent', 'OptanonAlertBoxClosed'])
    
    #  Patterny Onetrust i GTM
    check_patterns_in_page_content(page_content, ONETRUST_PATTERNS, "OneTrust")
    check_patterns_in_page_content(page_content, GTM_PATTERNS, "GTM")
    
    # Zamknięcie chromium
    driver.quit()

# info dot. uruchomienie skryptu
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python headselcheck.py <adres_url>")
        sys.exit(1)
    url = sys.argv[1]
    main(url)
