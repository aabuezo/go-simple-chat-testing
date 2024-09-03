Feature: Login page

    Scenario: Verify login page in Simple Chat web page
        Given I launch the Chrome browser
        When I go to the home page
        Then I am redirected to the login page
        Then I can see the 'Simple Chat' title at the top

    Scenario: Verify that I can login successfully with correct credentials
        Given I am a valid Simple Chat user
        And I launch the Chrome browser
        When I go to the home page
        And I provide a valid username
        And I provide a valid password
        And I click the Login button
        Then I am redirected to the chat room page
        And I close Chrome browser

    Scenario: Verify that I cannot login successfully with incorrect password
        Given I am a valid Simple Chat user
        And I launch the Chrome browser
        When I go to the home page
        And I provide a valid username
        And I provide an invalid password
        And I click the Login button
        Then I get 'Invalid username or password'
        And I close Chrome browser

    Scenario: Verify that I cannot login successfully with incorrect username
        Given I am not a valid Simple Chat user
        And I launch the Chrome browser
        When I go to the home page
        And I provide an invalid username
        And I provide a valid password
        And I click the Login button
        Then I get 'Invalid username or password'
        And I close Chrome browser
    