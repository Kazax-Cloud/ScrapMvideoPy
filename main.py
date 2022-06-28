import requests
import json


def get_data():

    cookies = {
        'MVID_CITY_ID': 'CityCZ_1638',
        'MVID_GUEST_ID': '18806644819',
        'MVID_REGION_ID': '6',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '1',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'searchType2': '2',
        'flacktory': 'no',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_KLADR_ID': '7800000000000',
        'MVID_REGION_SHOP': 'S904',
        'MVID_GEOLOCATION_NEEDED': 'true',
        '__lhash_': '2fa9f9faa06d276f6539a20fb4229ffd',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SMSError': '',
        'authError': '',
        '_ga': 'GA1.2.1105673106.1656420320',
        '_gid': 'GA1.2.1563755390.1656420320',
        '_ym_uid': '1656420320501790358',
        '_ym_d': '1656420320',
        '_ym_isad': '2',
        'uxs_uid': '2b4da9e0-f6e0-11ec-a3b6-290e16a3bca4',
        'AF_SYNC': '1656420320493',
        'afUserId': '38081bf6-abb7-471b-bac9-af1bfdd4fdb9-p',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'pZCkv68PdwB4b9NfvF2m2QMcW1xy2hfLfcyWqnJDPjz2r3dvl1VH!-991729019',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
        'bIPs': '-826759811',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpZXhYLU1hP3ckX31XIi81OTlRRA18WnQcdHEMZ1UdYxdSFHwWPz8tMTk9JRkKPyl5QhsTGjhuJmBOWyhDVlZqJh8WfW8lUAwQXD5Ib2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC8/Zx5kS2ImQ1pJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0LIytw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpZXhYLU1hP3ckX31XIi81OTlRRA18WnQcdHEMZ1UdYxdSFHwWPz8tMTk9JRkKPyl5QhsTGjhuJmBOWyhDVlZqJh8WfW8lUAwQXD5Ib2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC8/Zx5kS2ImQ1pJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0LIytw==',
        'cfidsgib-w-mvideo': 'jlewmhh54Y+B4BBq8ONIDtIm/Peid3WK8JiHka3oB0IN5c1RQUHAfCZAMoGO3LDb0MhO7SPgA1GQtD6dDa5AFetSNf+0MesfgQcJeZdKdMrppA0IVeM0+8MX4Dubc7i4DLd9nH6gxdoLNHHJLNE6jauiad78CtYkdkz7',
        'cfidsgib-w-mvideo': 'jlewmhh54Y+B4BBq8ONIDtIm/Peid3WK8JiHka3oB0IN5c1RQUHAfCZAMoGO3LDb0MhO7SPgA1GQtD6dDa5AFetSNf+0MesfgQcJeZdKdMrppA0IVeM0+8MX4Dubc7i4DLd9nH6gxdoLNHHJLNE6jauiad78CtYkdkz7',
        'gsscgib-w-mvideo': '3cMilTaVWaxjeHYohMQIokikwt3yR/W1S0YH9cjlB2lNqDv59kXLFY3buMTGyuXkr+DJ75/QCPyFYcXNvUOSa1am+Mk9iJIQaod8CKHycETryhpmvLIwi1KsdJd51gzqeZQCwipPxramWc4h4019ZoqwnH0u8ZqZErEB4DZ9j5UbkxSbrOan0Cd8Fasi7qF3d3OJ3REc0Mu/q/iECQdXj6cmwtNcSRCcv2sxslU0XffFWtWkVFZe5qLIwsoLkQ==',
        'gsscgib-w-mvideo': '3cMilTaVWaxjeHYohMQIokikwt3yR/W1S0YH9cjlB2lNqDv59kXLFY3buMTGyuXkr+DJ75/QCPyFYcXNvUOSa1am+Mk9iJIQaod8CKHycETryhpmvLIwi1KsdJd51gzqeZQCwipPxramWc4h4019ZoqwnH0u8ZqZErEB4DZ9j5UbkxSbrOan0Cd8Fasi7qF3d3OJ3REc0Mu/q/iECQdXj6cmwtNcSRCcv2sxslU0XffFWtWkVFZe5qLIwsoLkQ==',
        'fgsscgib-w-mvideo': 'WQM632b375247f8331f994a59a57fb1a9e670091',
        'fgsscgib-w-mvideo': 'WQM632b375247f8331f994a59a57fb1a9e670091',
        'cfidsgib-w-mvideo': 'S0ABOMz+gJCwCo0M8VBxiWzkn15/ceMlWHH6uzXALcMt+noYOAxBBL7OhLFAXk5iX9sUWRKkVyVL0VHQFaHh0fckGKfB85VCHKrITDSu0j0p8ZGxLqhA+pT3c1lxqYbG+RSgns/TEmyR1u7OKpx5y4HY6LfY0z173cl8',
        'MVID_ENVCLOUD': 'primary',
        'CACHE_INDICATOR': 'false',
        'ADRUM_BT': 'R:98|g:630a9a8e-4c6a-4aaa-8b12-36fe0522827f2413511',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'MVID_CITY_ID=CityCZ_1638; MVID_GUEST_ID=18806644819; MVID_REGION_ID=6; MVID_CART_MULTI_DELETE=false; MVID_CHECKOUT_REGISTRATION_AB_TEST=1; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; searchType2=2; flacktory=no; MVID_TIMEZONE_OFFSET=3; MVID_KLADR_ID=7800000000000; MVID_REGION_SHOP=S904; MVID_GEOLOCATION_NEEDED=true; __lhash_=2fa9f9faa06d276f6539a20fb4229ffd; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SMSError=; authError=; _ga=GA1.2.1105673106.1656420320; _gid=GA1.2.1563755390.1656420320; _ym_uid=1656420320501790358; _ym_d=1656420320; _ym_isad=2; uxs_uid=2b4da9e0-f6e0-11ec-a3b6-290e16a3bca4; AF_SYNC=1656420320493; afUserId=38081bf6-abb7-471b-bac9-af1bfdd4fdb9-p; wurfl_device_id=generic_web_browser; JSESSIONID=pZCkv68PdwB4b9NfvF2m2QMcW1xy2hfLfcyWqnJDPjz2r3dvl1VH!-991729019; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpZXhYLU1hP3ckX31XIi81OTlRRA18WnQcdHEMZ1UdYxdSFHwWPz8tMTk9JRkKPyl5QhsTGjhuJmBOWyhDVlZqJh8WfW8lUAwQXD5Ib2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC8/Zx5kS2ImQ1pJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0LIytw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpZXhYLU1hP3ckX31XIi81OTlRRA18WnQcdHEMZ1UdYxdSFHwWPz8tMTk9JRkKPyl5QhsTGjhuJmBOWyhDVlZqJh8WfW8lUAwQXD5Ib2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC8/Zx5kS2ImQ1pJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0LIytw==; cfidsgib-w-mvideo=jlewmhh54Y+B4BBq8ONIDtIm/Peid3WK8JiHka3oB0IN5c1RQUHAfCZAMoGO3LDb0MhO7SPgA1GQtD6dDa5AFetSNf+0MesfgQcJeZdKdMrppA0IVeM0+8MX4Dubc7i4DLd9nH6gxdoLNHHJLNE6jauiad78CtYkdkz7; cfidsgib-w-mvideo=jlewmhh54Y+B4BBq8ONIDtIm/Peid3WK8JiHka3oB0IN5c1RQUHAfCZAMoGO3LDb0MhO7SPgA1GQtD6dDa5AFetSNf+0MesfgQcJeZdKdMrppA0IVeM0+8MX4Dubc7i4DLd9nH6gxdoLNHHJLNE6jauiad78CtYkdkz7; gsscgib-w-mvideo=3cMilTaVWaxjeHYohMQIokikwt3yR/W1S0YH9cjlB2lNqDv59kXLFY3buMTGyuXkr+DJ75/QCPyFYcXNvUOSa1am+Mk9iJIQaod8CKHycETryhpmvLIwi1KsdJd51gzqeZQCwipPxramWc4h4019ZoqwnH0u8ZqZErEB4DZ9j5UbkxSbrOan0Cd8Fasi7qF3d3OJ3REc0Mu/q/iECQdXj6cmwtNcSRCcv2sxslU0XffFWtWkVFZe5qLIwsoLkQ==; gsscgib-w-mvideo=3cMilTaVWaxjeHYohMQIokikwt3yR/W1S0YH9cjlB2lNqDv59kXLFY3buMTGyuXkr+DJ75/QCPyFYcXNvUOSa1am+Mk9iJIQaod8CKHycETryhpmvLIwi1KsdJd51gzqeZQCwipPxramWc4h4019ZoqwnH0u8ZqZErEB4DZ9j5UbkxSbrOan0Cd8Fasi7qF3d3OJ3REc0Mu/q/iECQdXj6cmwtNcSRCcv2sxslU0XffFWtWkVFZe5qLIwsoLkQ==; fgsscgib-w-mvideo=WQM632b375247f8331f994a59a57fb1a9e670091; fgsscgib-w-mvideo=WQM632b375247f8331f994a59a57fb1a9e670091; cfidsgib-w-mvideo=S0ABOMz+gJCwCo0M8VBxiWzkn15/ceMlWHH6uzXALcMt+noYOAxBBL7OhLFAXk5iX9sUWRKkVyVL0VHQFaHh0fckGKfB85VCHKrITDSu0j0p8ZGxLqhA+pT3c1lxqYbG+RSgns/TEmyR1u7OKpx5y4HY6LfY0z173cl8; MVID_ENVCLOUD=primary; CACHE_INDICATOR=false; ADRUM_BT=R:98|g:630a9a8e-4c6a-4aaa-8b12-36fe0522827f2413511',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera GX";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58',
        'x-set-application-id': 'bcc2e1e0-c36c-44cb-8922-2ad08e36d2a1',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    
    
    
    products_ids = response.get('body').get('products')
    
    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    
    
    
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        
    
    products_ids_str = ','.join(products_ids)
    
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    
    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        
    items_prices = {}
    
    material_prices = response.get('body').get('materialPrices')
    
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')
        
        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
        
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)
        

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)
        
    products_data = products_data.get('body').get('products')
    
    for item in products_data:
        product_id = item.get('productId')
        
        if product_id in products_prices:
            prices = products_prices[product_id]
            
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
        
    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)
    

def main():
    get_data()
    get_result()
    
    
if __name__ == '__main__':
    main()
