Feature: Login page

    Background: Common steps
        Given I launch the Chrome browser
        When I go to the home page

    Scenario: Verify login page in Simple Chat web page
        Then I am redirected to the login page
        And I can see the 'Simple Chat' title at the top

    Scenario Outline: Verify that I can login successfully with correct credentials
        When I provide a valid "<username>" and "<password>"
        And I click the Login button
        Then I am redirected to the chat room page
        And I close Chrome browser
    
    Examples:
        | username  | password |
        | John      | password |
        | Anna      | password |
        | Barney    | password |
        | Janeth    | password |
        | Luka      | password |
        | Stacey    | password |

    Scenario: Verify that I cannot login successfully with incorrect password
        When I provide a valid username "<John>"
        And I provide an invalid password
        And I click the Login button
        Then I get 'Invalid username or password'
        And I close Chrome browser

    Scenario: Verify that I cannot login successfully with incorrect username
        When I provide an invalid username
        And I provide a valid password
        And I click the Login button
        Then I get 'Invalid username or password'
        And I close Chrome browser
    