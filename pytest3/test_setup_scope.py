import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
	print('\nSetUp Session!')

@pytest.fixture(scope="module", autouse=True)
def setupModule():
	print('\nSetUp Module!')

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
	print('\nSetUp Function!')

def test1():
	print("\nExecuting test1!")
	assert True

def test2():
	print("\nExecuting test2!")
	assert True





