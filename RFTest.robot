*** Settings ***
Documentation    All tests contain a workflow constructed from keywords in
...              ''RobotFrameworkLibrary.py''. Tests check next things:
...               authentication checks at different user, password
...               Check any header in the returned response / get
...               Check the number of rows returned in the query / stream
...               Checking the return code for all the answers

Library     RobotFrameworkLibrary.py    ${VALID_USERNAME}    ${VALID_PASSWORD}
*** Variables ***
${VALID_USERNAME}    Anton
${VALID_PASSWORD}    123456

*** Test Cases ***
Valid login and password
    Basic auth  Anton  123456
    Status Should Be Equal    ${200}


Invalid user
    Basic auth  Toha  123456
    Status Should Be Equal    ${401}

Invalid password
    Basic auth  Anton  11123456
    Status Should Be Equal    ${401}

Header Return
    Get  Cookie  4123
    Header Should Be  Cookie  4123

Failing Header
    Get  Cookie  4123
    Should Have Header    TOHA

Get stream
    Stream  12
    Stream Should Be  ${12}

Third simple request1
    Stream  200
    Stream Should Be  ${100}