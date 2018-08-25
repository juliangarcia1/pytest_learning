#####
# test_handler.py
#Mock() -> unittest
#Mock() -> pytest

newpath = tempfile.mkdtemp(local_path + "template_ecs_status.xml")
res = handler(params, **{"path": newpath})


def hola():
    # logica 1
    # logica 2
    # logica 3
    return "algo"


m = Mock()
m.return_value = "algo"

res = hola()
assert res == m.return_value



######################
#-> INVESTIGAR:
#-> mock, MagicMock, diferencia entre patch de unittest y monkeypatch de pytest
#-> assert Pytest vs assert unittest
#-> pytest.raises Pytest vs self.assertRaise() unittest
#-> desventajas de pytest vs unittest
#conftest.py
@pytest.fixture(scope="module")
def api(pause):
    pause
    from ottmsc.utils.api_encoding import APIEncoding
    return APIEncoding('some_id', 'some_key')

@pytest.fixture -> qué pasa si llamas a api como parametro?
def pause():
    import time
    time.sleep(3)
    print("done")

@pytest.fixture
def create_db():
    # engine existe-> mongo/psql/mysql
    obj = engine.create_database("pruebitas")
    yield 
    obj.destroy()

######################
#test.py

class TestApiEncoding(object):

    def test_action_get_status_on_success(self, api, create_db):
        name = "GetStatus"
        media_id = '123456789'
        expected = {"some": "status_dict"}
        res = api.action(name, media_id)

    def foo():

    def foo_return_1():
    ...
    def foo_return_20():

#######
#test_integration.py

class TestBarWithApiEncodingIntegration():

    def bar_is_true(api): -> es necesario si ya está en el otro archivo?
        api.action()

    def bar_return_1():
    ...
    def bar_return_20():

#project/
#    - app/
#    - tests/
#        - fixtures/ -> ? se puede importar sin usar conftest.py?
#            - myfix.py ->?
#            - my2fix.py ->?
#
#        - unit/
#            - conftest.py -> api fixture
#            - test.py
#        - integration/
#            - conftest.py -> date fixture
#        - acceptance/


@pytest.fixture(scope="module")
def date():
    import datetime
    return datetime.datetime.now()
