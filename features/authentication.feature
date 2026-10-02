Feature: SauceDemo login page

    Scenario: Login page displays the required elements
        Given I open the SauceDemo login page
        Then the login page title should be "Swag Labs"
        And the username field should be visible
        And the password field should be visible
        And the login button should be visible