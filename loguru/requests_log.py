import requests
from loguru import logger
import time

def res_log(url):
        logger.info(f"Url = {url}")   
        time_b= time.time()       
        response = requests.get(url)
        logger.info(f"Response: {response.status_code}")
        time_a= time.time()
        logger.info(f"Time: {time_a - time_b} sec.")

        return response.text

res_log(url = 'https://www.olx.ua/d/uk/transport/legkovye-avtomobili/q-%D0%B0%D0%B2%D1%82%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B7%D1%81%D1%83/?utm_campaign=avto_dlya_zsu&utm_medium=virtual_category&utm_source=olx')