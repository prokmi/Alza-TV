# Created by prokmi at 5/2/2021
Feature: Alza.cz
  Testing one of the most popular Czech e-shops out there.

  Scenario: Add two most expensive TVs to cart
    Given I navigate to Alza.cz page
    When I open monitors section
    Then I sort the section by most expensive
    When I add 2 of most expensive products
    #And I navigate to cart
    #Then I can see 2 products in the cart
    When I wait 10 seconds
