@deleteProject
Feature: Verify CRUD operations for Project

  @deleteProject
  Scenario: Validate POST method - Project
    Given I send a POST request to /projects
  '''
  {
  "name" : "behave project test-02"
  }
  '''
    Then I expect status code 200
    And I expect the response match with the schema project_schema.json
    And I expect the response match with the send data
  '''
  {
  "name" : "behave project test-02"
  }
  '''
    And I expect the project Account should be the default one JALA
