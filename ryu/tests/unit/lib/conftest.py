import os
import pytest


@pytest.fixture(autouse=True)
def chdir_to_unit(request):
    """test_import_module.py uses relative paths like ./lib/test_mod/...
    that are relative to ryu/tests/unit/, so set cwd there."""
    if request.fspath.basename != 'test_import_module.py':
        yield
        return
    unit_dir = os.path.dirname(os.path.dirname(request.fspath))
    old = os.getcwd()
    os.chdir(unit_dir)
    yield
    os.chdir(old)
