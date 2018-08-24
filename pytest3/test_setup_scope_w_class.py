import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule():
	print('\nSetUp Module!')

@pytest.fixture(scope="class", autouse=True)
def setupSession():
	print('\nSetUp Class!')

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
	print('\nSetUp Function!')

class TestClass:
	def test1(self):
		print("\nExecuting test1!")
		assert True
	def test2(self):
		print("\nExecuting test2!")
		assert True





