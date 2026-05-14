import os
import pytest


@pytest.fixture(autouse=True)
def chdir_to_app(request):
    """test_tester.py uses relative paths like ../switch/of13/...
    that are relative to ryu/tests/unit/app/, so set cwd there."""
    if request.fspath.basename != 'test_tester.py':
        yield
        return
    unit_dir = os.path.dirname(os.path.dirname(request.fspath))
    old = os.getcwd()
    os.chdir(unit_dir)
    yield
    os.chdir(old)
