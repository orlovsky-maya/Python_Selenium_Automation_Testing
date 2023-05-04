import pytest


# Fixture for each function
@pytest.fixture()
def set_up():
    print('Login')
    yield
    print('Log out')


# Fixture for each module
@pytest.fixture(scope='module')
def start_module():
    print('Start')
    yield
    print('Finish')


# Fixture for each function
@pytest.fixture(scope='function')
def start_function():
    print('Function is started')
    yield
    print('Function is finished')

# Fixture for each class
# @pytest.fixture(scope='class')
# def start_class():
#     print('Function is started')
#     yield
#     print('Function is finished')



