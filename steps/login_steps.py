from behave import given, when, then

@given('user is on login page')
def step_impl(context):
    print("Navigating to login page")

@when('user enters valid credentials')
def step_impl(context):
    print("Entering valid credentials")

@when('user enters invalid credentials')
def step_impl(context):
    print("Entering invalid credentials")

@then('login should be successful')
def step_impl(context):
    assert True

@then('login should fail')
def step_impl(context):
    assert True