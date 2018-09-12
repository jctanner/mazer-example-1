import pytest

from ansible.modules.newmodule import do_foo


def test_do_foo():
    assert do_foo()
