import sys
import csv
import time
import datetime
import requests
sys.path.insert(0, '../../')

# name of csv file with product data
PRODUCTS_FILENAME = 'best_buy_products.csv'

# absolute path of csv file with product data
PRODUCTS_LOCAL_PATH = '/home/tarunam_verma/gcp-search/extract_data/best_buy_products.csv'

# url of web application which server autocomplete
WEBAPP_URL = 'http://tarunam-gcp-explore.appspot.com'

UPLOAD_URL = WEBAPP_URL + '/upload_bulk'

with open(PRODUCTS_LOCAL_PATH) as f:
    csv_reader = csv.DictReader(f, fieldnames=(
        'sku', 'name', 'regularPrice', 'salePrice', 'type', 'url', 'image', 'inStoreAvailability'))
    total_count = 0
    c = 0
    skip_lines = 0
    item_lst = []
    for line in csv_reader:
        total_count += 1
        if total_count < skip_lines:
            continue
        c += 1
        item_lst.append({
            'sku': line['sku'],
            'name': line['name']
        })
        if c == 200:
            r = requests.post(UPLOAD_URL, json=item_lst)
            if r.status_code != 200:
                print r.text
                break
            time.sleep(2)
            c = 0
            item_lst = []

        if not total_count % 10000:
            print total_count, datetime.datetime.now()
