import requests

async def  count_words_at_url(url,**kwargs):
    print("count_words_at_url",url)
    resp = requests.get(url)
    print(kwargs)
    print(resp.text)
    return len(resp.text.split())

async def  count_words_at_urlv2(**kwargs):
    resp = requests.get(kwargs.get("url"))
    print(kwargs)
    print(resp.text)
    return len(resp.text.split())

async def generate_report():
    print("generate_report")
    return "this is a demo {0} ".format("dalong")


async def task1(x, y):
    result = x + y
    return result

async def task2(previous_result):
    result = previous_result * 2
    return result