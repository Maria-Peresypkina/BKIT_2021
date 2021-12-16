from behave import *
from TDD_test import *

@given("Clothes_Builder")
def first_step(context):
    context.a = Clothes_Builder_Test()

@when("test_HM_builder return OK")
def test_HM_builder(context):
    context.a.test_HM()

@when("test_Bershka_builder return OK")
def test_Bershka_builder(context):
    context.a.test_Bershka()

@then("Good job")
def last_step(context):
    pass