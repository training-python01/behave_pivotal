Feature: Verify CRUD operation for Story

  Background: Create story as precondition
    Given I send a POST request to /projects
  '''
  {
  "name" : "behave project test-01"
  }
  '''
    When I save the response ID as project_id
    Then I expect status code 200

    Given I send a POST request to /projects/{context.project_id}/stories
  '''
  {
  "name" : "behave story test-01"
  }
  '''
    When I save the response ID as story_id
    Then I expect status code 200

  @deleteProject
  Scenario: Validate GET method - Story
    Given I send a GET request to /projects/{context.project_id}/stories
    Then I expect status code 200

  @deleteProject
  Scenario: Validate PUT method - Story
    Given I send a PUT request to /projects/{context.project_id}/stories/{context.story_id}
  '''
  {
  "name" : "Behave Story test-01 - Updated"
  }
  '''
    Then I expect status code 200

  @deleteProject
  Scenario: Validate DELETE method - Project
    Given  I send a DELETE request to /projects/{context.project_id}/stories/{context.story_id}
    Then I expect status code 204