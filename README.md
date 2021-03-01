# Test Automation Assignment - Trello Webpage


Implemented using Python and Selenium Page Object Model (POM).

### Project Folder Structure

    .
    ├── config                   # Config python file
    ├── drivers                  # directory contains web drivers
    ├── locators                 # locator directory contains module to store all element locators
    ├── pages                    # pages directory contains class and methods for each pages
    ├── reports                  # output report will be stored
    ├── tests                    # main unittest file to be executed
    └── README.md

### Prerequisites

1. Install required python libraries using pip.
2. External Libraries used:
     - Selenium
     - HtmlTestRunner 
3. Installation Command: 
      - `pip install selenium`
      - `pip install html-testRunner`
   
3. Chrome driver and firefox drivers are present in the directory `../driver/`
   
### Steps to execute Python unit test:

1. To run Python unit tests:
   - `cd tests/`
   - `python -m unittest trello_automation_test.py`