
from behave import *


@when("I open {section} section")
def step_impl(context, section):
    context.page = context.page.open_section(section)
    context.page.wait_for()


@step("I sort the section by {sort_type}")
def step_impl(context, sort_type):
    if sort_type == "most expensive":
        context.page.sort_by(context.page.SortTypes.MOST_EXPENSIVE)
    else:
        raise NotImplementedError("Not implemented yet!")


@when("I add {number} of most expensive products")
def step_impl(context, number):
    context.page.add_most_expensive_products(int(number))
