from behave import *
from hamcrest import assert_that, is_not, empty, is_

from pages.alza_main_page import AlzaMainPage


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
    context.cart_items = context.page.add_most_expensive_products(int(number))


@when("I open the shopping cart")
def step_impl(context):
    if not isinstance(context.page, AlzaMainPage):
        context.page = AlzaMainPage(context.driver)
    context.page = context.page.open_cart()


@then("I can see correct products in the cart")
def step_impl(context):
    assert_that(context.cart_items, is_not(empty), "Cart items variable is empty!")
    # alza is an asshole and renames products in cart
    # assert_that(
    #     context.page.get_products_in_cart(), only_contains(context.cart_items),
    #     "Specified items weren't in cart!"
    # )
    # TODO find a better solution
    products = [
        expected in actual
        for expected in context.cart_items
        for actual in context.page.get_products_in_cart()
    ]
    products = [product for product in products if product]  # filter out only matches
    assert_that(
        len(products), is_(len(context.cart_items)), "The items in cart don't match!"
    )
