import pytest
import pathlib
from reqsit import main
from unittest.mock import Mock
from pytest_mock import MockFixture
import errno
import os

NAME = "test.txt"
CONTENT = ["foo==bar\n", "biz==baz\n", "brt==bop\n"]
CONV_CONTENT = ['"foo==bar",', '"biz==baz",', '"brt==bop",']


@pytest.fixture()
def reqs_file(tmp_path) -> pathlib.Path:
    filename = tmp_path / NAME
    with open(filename, "w") as f:
        f.writelines(CONTENT)

    return filename


@pytest.fixture()
def mock_glob_none(mocker: MockFixture) -> Mock:
    mock = mocker.patch("glob.glob")
    mock.return_value = []
    return mock


@pytest.fixture()
def mock_glob_found(mocker: MockFixture, reqs_file) -> Mock:
    mock = mocker.patch("glob.glob")
    mock.return_value = [reqs_file]
    return mock


def test_read(reqs_file) -> None:
    contents = main.read_reqs(reqs_file)
    assert contents == CONTENT


def test_convert() -> None:
    conv = main.convert_reqs(CONTENT)
    assert conv == CONV_CONTENT


def test_fire_found(mock_glob_found) -> None:
    reqs = main.fire_wrapper(NAME)
    assert reqs == CONV_CONTENT


def test_fire_none(mock_glob_none) -> None:
    with pytest.raises(FileNotFoundError) as execinfo:
        reqs = main.fire_wrapper(NAME)
    assert execinfo.value.args[0] == errno.ENOENT
    assert execinfo.value.args[1] == os.strerror(errno.ENOENT)
