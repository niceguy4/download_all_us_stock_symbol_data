## Download stock symbol data from nasdaqtrader

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

