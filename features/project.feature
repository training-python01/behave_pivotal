Feature: Verify CRUD operations for Project
  Scenario: Validate GET method - Project
    Given I make a GET request to /projects
    Then I expect status code 200

  Scenario: Validate POST method - Project
    Given I make a POST request to /projects
    '''
    {
      "name" : "behave project test-01"
    }
    '''
    Then I expect status code 200

   Scenario: Validate PUT method - Project
     Given I make a POST request to projects
     '''
      {
        "name" : "Behave project test-01"
      }
      '''
     When I save the response ID as project_id
     Given I make a PUT request to projects/{context.project_id}
      '''
      {
        "name" : "Behave project test-01 - Updated"
      }
      '''
     Then I expect status code 200
