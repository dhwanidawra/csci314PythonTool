import requests
import time

retries = range(1,6)
waitlength = 0.5

operation_name = ''
url = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'
headers = {
        'X-EBAY-SOA-SECURITY-APPNAME':'JoshuaRe-CSIT314T-SBX-d2eb49443-1f81d300',
        'X-EBAY-SOA-RESPONSE-DATA-FORMAT':'json'
}

def fetch_results_keyword(keywords, entries, pageNumber):
    headers['X-EBAY-SOA-OPERATION-NAME'] = 'findItemsByKeywords'
    params = {
        'keywords': keywords,
        'paginationInput.entriesPerPage': entries,
        'paginationInput.pageNumber': pageNumber
    }

    for i in retries:
        try:
            response = requests.get(url, headers=headers, params=params)
            response_object = response.json()
        except requests.exceptions.RequestException as e:
            if i < 5:
                print("Attempt " + str(i) + ' of 5 - error connecting. Retrying...')
                time.sleep(waitlength)
                continue
            else:
                print("Attempt " + str(i) + ' of 5 - error connecting: \n', e)
                response_object = None
        break

    return response_object

def fetch_results_category(categoryId, entries, pageNumber):
    headers['X-EBAY-SOA-OPERATION-NAME'] = 'findItemsByCategory'
    params = {
        'categoryId': categoryId,
        'paginationInput.entriesPerPage': entries,
        'paginationInput.pageNumber': pageNumber
    }

    for i in retries:
        try:
            response = requests.get(url, headers=headers, params=params)
            response_object = response.json()
        except requests.exceptions.RequestException as e:
            if i < 5:
                print("Attempt " + str(i) + ' of 5 - error connecting. Retrying...')
                time.sleep(waitlength)
                continue
            else:
                print("Attempt " + str(i) + ' of 5 - error connecting: \n', e)
                response_object = None
        break

    return response_object

def fetch_results_advanced(keywords, categoryId, entries, pageNumber):
    headers['X-EBAY-SOA-OPERATION-NAME'] = 'findItemsAdvanced'
    params = {
        'keywords': keywords,
        'categoryId': categoryId,
        'paginationInput.entriesPerPage': entries,
        'paginationInput.pageNumber': pageNumber
    }
    
    for i in retries:
        try:
            response = requests.get(url, headers=headers, params=params)
            response_object = response.json()
        except requests.exceptions.RequestException as e:
            if i < 5:
                print("Attempt " + str(i) + ' of 5 - error connecting. Retrying...')
                time.sleep(waitlength)
                continue
            else:
                print("Attempt " + str(i) + ' of 5 - error connecting: \n', e)
                response_object = None
        break

    return response_object