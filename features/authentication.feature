Feature: SauceDemo login page

    Scenario: Login page displays the required elements
        Given I open the SauceDemo login page
        Then the login page title should be "Swag Labs"
        And the username field should be visible
        And the password field should be visible
        And the login button should be visible

    Scenario: Valid user can log in
        Given I open the SauceDemo login page
        When I log in with username "standard_user" and password "secret_sauce"
        Then I should be on the poducts page