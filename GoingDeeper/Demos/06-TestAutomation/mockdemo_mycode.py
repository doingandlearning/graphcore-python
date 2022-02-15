from mockdemo_dependencies import BASE_URL
from mockdemo_dependencies import calculate_meaning_of_life
from mockdemo_dependencies import DataLoader


def build_url(**kwargs):
    url = BASE_URL
    if len(kwargs) != 0:
        url += "?"
        for k, v in kwargs.items():
            url += "{}={}&".format(k,v)
        url = url.rstrip('&')
    return url


def get_meaning_of_life():
    result = calculate_meaning_of_life()
    return 'The meaning of life is ' + str(result)


def get_product():
    dataLoader = DataLoader()
    result = dataLoader.load_product()
    return 'Product is ' + str(result)
