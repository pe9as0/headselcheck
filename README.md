# README 📄 
Cookie & Tag Presence Checker (Selenium, headless)
A small Python utility that loads a web page in headless Chromium (Selenium) and verifies:

- required cookies (e.g., OptanonConsent, OptanonAlertBoxClosed),
- OneTrust patterns in page source (e.g., OneTrust, cdn.cookielaw.org, otSDKStub.js),
- Google Tag Manager patterns (e.g., googletagmanager.com/gtm.js, GTM-, SiteLocalContainer).

Ideal for quick compliance checks and basic instrumentation validation.

# What it checks ✅ 

Cookies: presence and values for given cookie names.

Page source: substring pattern matches for OneTrust & GTM.


# Requirements 🧩 

Python 3.x

Chromium / Chrome + matching chromedriver

Packages: selenium, webdriver-manager (optional)

Install (example):
```pip install selenium webdriver-manager```

ℹ️ Script default path to chromedriver: ```/usr/bin/chromedriver```.


# Usage 🚀
```python3 selescan.py <url>```
Example:
```python3 selescan.py https://example.com```
Output (stdout) will list:

- found/missing cookies (OptanonConsent, OptanonAlertBoxClosed),
- found/missing OneTrust patterns,
- found/missing GTM patterns.


# Config (quick edit) ⚙️ 

Cookie names to verify: edit the list in check_cookies(...) call.
Patterns: edit ONETRUST_PATTERNS and GTM_PATTERNS.


# Notes / Good practices 🔒 

Headless mode is enabled by default.
The script currently waits a fixed time.sleep(4) for page load; for SPAs you may want to replace it with Selenium explicit waits (e.g., WebDriverWait on a known selector) or increase the delay.
If the site sets cookies after consent or async, consider:

- waiting for the CMP frame to load,
- clicking “Accept” via Selenium before reading cookies,
- re‑reading cookies after actions.

# Possible improvements (optional) 💡 

Add CLI flags: --cookies, --patterns-file, --wait-seconds, --headful.

Support regex patterns (not only substring).

Structured JSON output (--json) for CI pipelines.

Exit codes (e.g., non‑zero if any required item is missing).

Add webdriver-manager path usage:

```service = Service(ChromeDriverManager().install())```

