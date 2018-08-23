class TestClass:
		@classmethod
		def setup_class(cls):
			print('\nSetUp TestClass!')
			
		@classmethod
		def teardown_class(cls):
			print('\nTearDown TestClass!')

		def setup_method(self, method):
			if method == self.test1:
				print("\nSetting up test 1!")
			elif method == self.test2:
				print("\nSetting up test2!")
			else:
				print("\nSetting up unknow test!")

		def teardown_method(self, method):
			if method == self.test1:
				print("\nTearing down test1!")
			elif method == self.test2:
				print("\nTearing down test2!")
			else:
				print("\nTearing down unknow test!")


		def test1(self):
			print("\nExecuting test1!")
			assert True


		def test2(self):
			print("\nExecuting test2!")
			assert True





