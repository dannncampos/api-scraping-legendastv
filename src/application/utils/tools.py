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
    """
    Create a hash string for IDs
    Return: the hash string
    """
    return hashlib.md5((datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')).encode()).hexdigest()


def extract_date(date):
    """
    Extract date from a string
    date: The entire string with date
    Return: The date in a ISO 8601 format (yyyy-MM-dd)
    Raises:
        Exception: Invalid string for parser
    """
    match = re.search(r'(?P<d>\d{2})\/(?P<m>\d{2})\/(?P<y>\d{4})', date)
    if match is not None:
        return match['y']+'-'+match['m']+'-'+match['d']
    raise Exception(f"It can not extract date of {date}")


def extract_only_integers(data):
    """
    Extract integers from a string
    data: The entire string with integers
    Return: Only integers
    Raises:
        Exception: Invalid string for parser
    """
    data = re.sub(r'[^\d]', '', data)
    if data is not None:
        return int(data)
    raise Exception(f"It can not extract date of {data}")
