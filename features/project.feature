Feature: Verify CRUD operations for Project

  Background: create project as precondition
    Given I make a POST request to /projects
    '''
    {
    "name" : "behave project test-01"
    }
    '''
    When I save the response ID as project_id
    Then I expect status code 200

  Scenario: Validate GET method - Project
    Given I make a GET request to /projects
    Then I expect status code 200

  Scenario: Validate POST method - Project
    Given I make a POST request to /projects
    '''
    {
    "name" : "behave project test-02"
    }
    '''
    Then I expect status code 200
    And I expect the response match with the schema project_schema.json

  Scenario: Validate PUT method - Project
    Given I make a PUT request to projects/{context.project_id}
    '''
    {
    "name" : "Behave project test-01 - Updated"
    }
    '''
    Then I expect status code 200

  Scenario: Validate DELETE method - Project
    Given  I make a DELETE request to projects/{context.project_id}
    Then I expect status code 204
