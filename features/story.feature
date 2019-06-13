Feature: Verify CRUD operation for Story
  Background: Create story as precondition
    Given I make a POST request to /projects
    '''
    {
    "name" : "behave project test-01"
    }
    '''
    When I save the response ID as project_id
    Then I expect status code 200

    Given I make a POST request to /projects/{context.project_id}/stories
    '''
    {
    "name" : "behave story test-01"
    }
    '''
    When I save the response ID as story_id
    Then I expect status code 200


  Scenario: Validate GET method - Story
    Given I make a GET request to /projects/{context.project_id}/stories
    Then I expect status code 200

  Scenario: Validate POST method - Story
    Given I make a POST request to /projects/{context.project_id}/stories
    '''
    {
    "name" : "behave story test-01"
    }
    '''
    Then I expect status code 200

  Scenario: Validate PUT method - Story
    Given I make a PUT request to projects/{context.project_id}/stories/{context.story_id}
    '''
    {
    "name" : "Behave Story test-01 - Updated"
    }
    '''
    Then I expect status code 200

  Scenario: Validate DELETE method - Project
    Given  I make a DELETE request to projects/{context.project_id}/stories/{context.story_id}
    Then I expect status code 204