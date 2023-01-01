import requests


def get_age(name) -> int:
    resp = requests.get("https://api.agify.io", params={'name': name})
    return int(resp.json()['age'])


def get_nationalities(name) -> list:
    resp = requests.get("https://api.nationalize.io", params={'name': name})
    return [ c['country_id'] for c in resp.json()['country']]


def get_gender(name) -> str:
    resp = requests.get("https://api.genderize.io", params={'name': name})
    return resp.json()['gender']
