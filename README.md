## Download stock symbol data from nasdaqtrader

About:

This script downloads U.S. stock symbol data from nasdaqtrader's ftp server. The follow data is included:
1. Symbol Name
2. Security Name
3. market Category
4. Test Issue (no idea what this is)
5. Financial Status
6. Round Lot Size (rls in databse)
7. ETF (yes or no)
8. Nextshares

[Nasdaqtrader Descriptions](http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs)

* Downloads from FTP server at nasdaqtrader
* Saves list to CSV
* Ports CSV list to SQL database

Script Actions:
* Pulls file list from ftp://nasdaqtrader.com/
* Saves data to CSV on local machine (your computer)
* Combines lists
* Saves data stock_symbol_data.sqlite

Python Library Requirements (defaults):
shutil
urllib
contextlib
csv
sqlite3

