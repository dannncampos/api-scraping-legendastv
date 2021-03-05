from contextlib import contextmanager

@contextmanager
def does_not_raise():
    yield


def check_return(input_, expected, in_comp=False):
    if not in_comp:
        assert input_ == expected
    else:
        assert input_ in expected


def assert_bool(bool_):
    assert bool_


def check_raise(context, function, *args, **kwargs):
    with context:
        try:
            assert function(*args, **kwargs) is not None
        except AssertionError:
            assert function(*args, **kwargs) is None
