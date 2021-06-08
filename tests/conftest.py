from stuff.accum import Accumulator
import pytest

@pytest.fixture
def accum():
  return Accumulator()