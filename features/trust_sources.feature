@browser
Feature: Sources are not outdated

  Scenario: A wiki nearby search
    Given I visit "https://en.wikipedia.org/wiki/Special:Nearby" with title "Nearby"
    When I search by "43.3890968" and "-4.3823338" coords using wiki nearby API
    Then I should see "San Vicente de la Barquera" in the wiki nearby results page
    Then I should see "Valdáliga" in the wiki nearby results page
    Then I should see "Val de San Vicente" in the wiki nearby results page


  Scenario: A wiki opensearch search
    Given I visit "https://en.wikipedia.org/wiki/Special:Nearby" with title "Nearby"
    When I search by "43.3890968" and "-4.3823338" coords using wiki nearby API
    Then I should see "San Vicente de la Barquera" in the wiki nearby results page
    Then I should see "Valdáliga" in the wiki nearby results page
    Then I should see "Val de San Vicente" in the wiki nearby results page