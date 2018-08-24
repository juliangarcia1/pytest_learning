import pytest

@pytest.fixture()
def setup1():
	print('\nSetUp!')
	yield
	print("\nTearDown using yield!")

@pytest.fixture()
def setup2(request):
	print('\nSetUp!')
	
	def teardown_a():
		print("\nTearDownA using addfinalizer!")

	def teardown_b():
		print("\nTearDownB using addfinalizer!")

	request.addfinalizer(teardown_a)
	request.addfinalizer(teardown_b)

def test1(setup1):
	print("\nExecuting test1!")
	assert True

def test2(setup2):
	print("\nExecuting test2!")
	assert True





