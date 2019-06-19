@deleteProject
Feature: Verify CRUD operations for Project

  Background: create project as precondition
    Given I send a POST request to /projects
  '''
  {
  "name" : "behave project test-01"
  }
  '''
    When I save the project response
    Then I expect status code 200

  @deleteProject
  Scenario: Validate GET method - Project
    Given I send a GET request to /projects
    Then I expect status code 200

  @deleteProject
  Scenario: Validate PUT method - Project
    Given I send a PUT request to /projects/{project.id}
  '''
  {
  "name" : "Behave project test-01 - Updated"
  }
  '''
    Then I expect status code 200

  @deleteProject
  Scenario: Validate DELETE method - Project
    Given  I send a DELETE request to /projects/{project.id}
    Then I expect status code 204
