# ============================================================================
# EXAMPLE ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s rs.1mxwiki.statistics -t test_example.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src rs.1mxwiki.statistics.testing.RS_1MXWIKI_STATISTICS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/rs/1mxwiki/statistics/tests/robot/test_example.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a member I want to be able to log into the website
  [Documentation]  Example of a BDD-style (Behavior-driven development) test.
  Given a login form
   When I enter valid credentials
   Then I am logged in


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a login form
  Go To  ${PLONE_URL}/login_form
  Wait until page contains  Login Name
  Wait until page contains  Password


# --- WHEN -------------------------------------------------------------------

I enter valid credentials
  Input Text  __ac_name  admin
  Input Text  __ac_password  secret
  Click Button  Log in


# --- THEN -------------------------------------------------------------------

I am logged in
  Wait until page contains  You are now logged in
  Page should contain  You are now logged in
