# pytest_learning
#### This is to learn some features of pytest
#### It is going to be just as a reference to 
#### some topics of pytest:

+ **pytest installation by pip**
+ **Test function**
+ **Test class**
+ **Basic pytest command line**

  pytest -v -s
  
  -v Shows verbose 
  
  -s Show output from tests
+ **Pytest decorator**
  + Scope
  
    The scope defines which part of the code the decorator is going to reach out.
  + Autouse
  
    This is a parameter specified in the decorator to indicate ?it is going to be use in the whole file/current scope?
  + SetUp
  
    The SetUp part of the test is going to be contained in the fixture decorator. All the code
    contained there is going to be executed at the beginning of the scope.
  + TearDown
    the TearDown part of the test is going to be declare inside the same fixture, the only that 
    we are going to use as delimiter or indicator is the yield reserved word or register a function
    using the request.addfinalizer function.
  
    + Yield
      
          @pytest.fixture
          def print_hello():
             print('Hello!')
	+ request.addfinalizer
