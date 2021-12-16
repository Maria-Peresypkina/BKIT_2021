from behave import *
from test.TDD_test import *

@given("I ho4y znat vvedenie dannie")
def pisKka(context):
    context.a = TestBot()


@when("I zapominau name")
def Zapominalka(context):
    context.a.test_1()

@when("I zapominau age")
def Zapominalka2(context):
    context.a.test_2()

@then("I xochy 4bee sovpalo!!!!")
def check_result(context):
    pass