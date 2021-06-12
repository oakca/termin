# termin
Berlin Service Portal - Schedule Termin Script
(works only on windows 10)

# Requirements
- Python 3.x
- Selenium
- Tor Browser
- chromedriver

# Installing
1) Clone the repository or download it
2) Install **Selenium** to your python environment via `pip install selenium`
3) Install **Tor Browser** to desktop from https://www.torproject.org/download/
4) Either use the **chromedriver** comes with this package, or download it from https://chromedriver.chromium.org/downloads

**Be careful to install the right chromedriver. The chromedriver comes with this repository works only with chrome version 91. You can check that by writing `chrome://settings/help` to your chrome adress tab**

# Usage (example with driver licence change termin)
1) Set the right Tor Browser path. (By default, it is set to `'C:\Users\---\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'` in line 38 in `main.py`)
2) Run `main.py`
3) Script will ask the termin url
4) **Example:** Open the following url: https://service.berlin.de/dienstleistung/327537/
5) Right click the `Termin berlinweit suchen` button
6) Copy link address
7) Paste it into the script
8) ENTER

# Termin
- When program finds a termin, it will stop and u will give your credentials. Voila!
