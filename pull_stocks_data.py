####################################################
#
# Downloads stock symbol data from nasdaqtrader ftp
# Write to CSV file & SQL file
#
####################################################

import shutil
import urllib.request as request
from contextlib import closing
import csv
import sqlite3

# files names on nasdaqtrader ftp site
grab_file_names = ['otherlisted', 'nasdaqlisted']

# download files from ftp and save as CSV
def load_stock_trickers(grab_file_names):
    try:
        for file in grab_file_names:
            with closing(request.urlopen('ftp://nasdaqtrader.com/Symboldirectory/' + str(file) + '.txt')) as r:
                with open(str(file) + '.csv', 'wb') as f:
                    shutil.copyfileobj(r, f)

    except Exception as e_log:
        print("Error during connect to ftp site.")
        print("Error log:", e_log)
        print("Exiting script")
        exit()

# create/delete dasebase
def create_db():
    conn = sqlite3.connect('stock_symbol_data.sqlite', timeout=30)
    cur = conn.cursor()

    cur.executescript('''DROP TABLE IF EXISTS stocks
    ''')

    cur.executescript('''
    CREATE TABLE stocks (
        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
        symbol TEXT,
        name TEXT,
        exchange TEXT,
        cqs_symbol TEXT,
        etf TEXT,
        rls TEXT,
        test_issue TEXT,
        nas_sym TEXT
    );
    ''')
    conn.commit()
    conn.close()

# parse csv data and write to databse
def symbols_to_db(stock_list_details):
    conn = sqlite3.connect('stock_symbol_data.sqlite', timeout=30)
    cur = conn.cursor()
    for detail in stock_list_details:
        cur.execute('''INSERT OR REPLACE INTO stocks (symbol, name, exchange, cqs_symbol, etf, rls, test_issue, nas_sym)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6], detail[7]))
    conn.commit()
    conn.close()

# load csv file data and combine information
def import_list(file_name):
    stock_list_details = []
    stock_list_details_temp = []
    for file in file_name:
        with open(str(file) + '.csv', newline='', ) as f:
            read_data = csv.reader(f, delimiter='|', quotechar='|')
            for row in read_data:
                stock_list_details_temp.append(row)
        # delete label information at the front/end of file
        del stock_list_details_temp[0]
        del stock_list_details_temp[(len(stock_list_details_temp)-1)]
        stock_list_details.extend(stock_list_details_temp)
        stock_list_details_temp = []
    f.closed
    return stock_list_details


print('Pulling ' + ', '.join(map(str, grab_file_names)) + ' from ftp nasdaqtrader...')
load_stock_trickers(grab_file_names)
print('Creating database: stock_tickers.sqlite')
create_db()

stock_list_details = import_list(grab_file_names)

print('Writing ' + str(len(stock_list_details)) + ' stock tickers database...')
symbols_to_db(stock_list_details)
print('Update complete.')
