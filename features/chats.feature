Feature: Login page

    Scenario Outline: Sender logs in
        Given I launch the Chrome browser
        When I go to the home page
        Then I am redirected to the login page
        And I can see the Simple Chat title at the top
        When I provide a valid "<username>" and "<password>"
        And I click the Login button
        Then I am redirected to the chat room page
        When I enter "<Barney>" as destinatary
        And I enter a message "<Hello, Barney!>" in the message field
        And I click the Send Message button
        Then I see the message "<Hello, Barney!>"
        When I click the logout link
        Then I am redirected to the login page
    
    Examples:
        | username  | password |
        | John      | password |

    Scenario Outline: Receiver logs in
        Given I launch the Chrome browser
        When I go to the home page
        Then I am redirected to the login page
        And I can see the Simple Chat title at the top
        When I provide a valid "<username>" and "<password>"
        And I click the Login button
        Then I am redirected to the chat room page
        And I see the message "Hello, Barney!"
        When I click the logout link
        Then I am redirected to the login page
        And I close Chrome browser
    
    Examples:
        | username  | password |
        | Barney    | password |