import pytest
from praktikum.bun import Bun


@pytest.fixture
def default_bun():
    return Bun("Стандартная булочка", 1.0)
