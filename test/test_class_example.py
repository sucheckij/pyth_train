import pytest

@pytest.fixture
def powitanie():
    print('Witaj w testach')
    yield
    print('Po testach')

@pytest.fixture(scope='class')
def powitanie_current_time(request):   # na wejsciu request jest klasa ktora opakowujemy "TestMultiTests"
    import datetime
    request.cls.now = datetime.datetime.utcnow()
    print("w klasie testy")
    yield
    print("koniec testow")


@pytest.mark.useFixtures('powitanie_current_time')
class TestMultiTests:
    # __test__ = False - olanie tej klasy w testach

    # @pytest.mark.useFixtures('powitanie')
    # def test_first(self):
    #     assert 5 == 5

    def test_second(self):
        assert 10 > 20

    def test_third(self):
        print('data startu', self.now)
        assert 20 == 10




