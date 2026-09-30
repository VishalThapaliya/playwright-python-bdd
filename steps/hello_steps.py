from pytest_bdd import given, then

@given("the BDD framework is configured")
def bdd_framework_is_configured():
    pass


@then("the test should run successfully")
def test_should_run_successfully():
    assert True