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

  @deleteProject
  Scenario: Validate POST method - Story
    Given I send a POST request to /projects/{context.project_id}/stories
  '''
  {
  "name" : "behave story test-01"
  }
  '''
    Then I expect status code 200
