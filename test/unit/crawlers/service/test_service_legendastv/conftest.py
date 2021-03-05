import mock
import pytest

from src.crawlers.legendastv.service.service_legendastv import ServiceLegendasTv


@pytest.fixture
def legendastv_service():
    return ServiceLegendasTv('Simpsons', 'User', 'Password')
