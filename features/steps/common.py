import time
from behave import *
from hamcrest import assert_that, is_

from pages.alza_main_page import AlzaMainPage


@given("I navigate to {page_name} page")
def step_impl(context, page_name):
    if page_name == "Alza.cz":
        # only supporting Alza right now - different solution would be used for multiple pages
        context.page = AlzaMainPage(context.driver)
    else:
        raise NotImplementedError("Unknown page selected!")
    context.driver.get(context.page.url)
    context.page.wait_for()


@then("I check whether every element is on the page")
def step_impl(context):
    assert_that(context.page.elm_check(), is_(True),
                "Some elements are missing on the current page!")


@when("I wait {seconds} seconds")
def step_impl(context, seconds):
    time.sleep(int(seconds))

