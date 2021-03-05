"""Tools to be used to help parse data from crawler"""
import re
import hashlib
from datetime import datetime
from unicodedata import normalize
import requests

def clear_content(content):
    """
    Remove tabs, new lines, backlashes from string data
    content: string data to be cleaned
    Return: string data cleaned
    """
    return re.sub(r'[\t\r\n\\"]', '', "".join(content)).strip()


def normalizer(content):
    """
    Normalize a string into ASCII encode
    content: string data to be normalized
    Return: string normalized
    """
    return normalize('NFKD', content).encode('ASCII', 'ignore').decode('ASCII')


def get_session():
    """
    Starts a requests session
    Return: the session required
    """
    return requests.Session()


def create_hash_md5():
    return hashlib.md5((datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')).encode()).hexdigest()


def extract_date(data):
    match = re.match('(?P<data>\d{2}\/\d{2}\/\d{4})', data)
    if match is not None:
        return match['data']
    print(f"It can not extract date of {data}")
    return data
