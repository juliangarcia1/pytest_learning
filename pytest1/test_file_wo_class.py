import pytest

@pytest.fixture()
def setup():
	print('\nSetUp!')
	

def test1(setup):
	print("\nExecuting test1!")
	assert True

@pytest.mark.usefixtures("setup")
def test2():
	print("\nExecuting test2!")
	assert True





