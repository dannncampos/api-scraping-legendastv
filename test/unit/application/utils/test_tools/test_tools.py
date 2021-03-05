from unittest.mock import patch, mock_open
from freezegun import freeze_time
from datetime import datetime
from os import remove
from json import load

import pytest
import pathlib

from src.application.utils import tools
from test import tools_for_testing
from test.unit.application.utils.test_tools.mock import expected_outputs, session_mock

# ================================


@pytest.mark.clear_content
def test_clear_content_check_raise():
    content = 'This is a sample text ready to be cleaned - some characters to be removed -> [\ \t \n \r]'
    tools_for_testing.check_raise(tools_for_testing.does_not_raise(), tools.clear_content, content)


@pytest.mark.clear_content
def test_clear_content_check_return():
    content = 'This is a sample text ready to be cleaned - some characters to be removed -> [\ \t \n \r]'
    tools_for_testing.check_return(tools.clear_content(content), expected_outputs.clear_content)


# ================================


@pytest.mark.get_session
@patch('requests.sessions.Session', side_effect=lambda _: session_mock.SessionMock())
def test_get_session_check_raise(_):
    tools_for_testing.check_raise(tools_for_testing.does_not_raise(), tools.get_session)


# ==============================


@pytest.mark.create_hash_md5
@freeze_time('2020-01-01')
def test_create_hash_md5_check_raise():
    tools_for_testing.check_raise(tools_for_testing.does_not_raise(), tools.create_hash_md5)


@pytest.mark.create_hash_md5
@freeze_time('2020-01-01')
def test_create_hash_md5_check_return():
    tools_for_testing.check_return(tools.create_hash_md5(), expected_outputs.create_hash_md5)


# ==============================


@pytest.mark.extract_date
@pytest.mark.parametrize(
    "input_,expected",
    [
        ('1/02/2019', tools_for_testing.does_not_raise()),
        ('01/02/2019', tools_for_testing.does_not_raise())
    ]
)
def test_extract_date_check_raise(input_, expected):
    tools_for_testing.check_raise(expected, tools.extract_date, input_)


@pytest.mark.extract_date
@pytest.mark.parametrize(
    "input_,expected",
    [
        ('1/02/2019', '2019-02-1'),
        ('01/02/2019', '2019-02-01')
    ]
)
def test_extract_date_check_return(input_, expected):
    tools_for_testing.check_return(tools.extract_date(input_), expected)
