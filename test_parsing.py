import requests




params = {
    'appType': '1',
    'curr': 'rub',
    'dest': '-1257786',
    'sort': 'popular',
    'spp': '30',
    'subject': '2290',
}

response = requests.get('https://catalog.wb.ru/catalog/electronic15/catalog', params=params, headers=headers)
print (response.status_code)
print(response.json())