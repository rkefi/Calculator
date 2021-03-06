# Calculator Test Automation

This is a test automation project for a web calculator.
The project uses Behave as test automation framework with the python programming language.

## Getting Started

To save time i've created a python virtual environment called "CalcTaskEnv" that contains all the python packages needed to run this project.

### Behave Project Structure

```bash
├── features                          # features folder that contains the feature files with the scenarios definition
│   ├── pages                         # Page Object Model definition for the calculator web page in python
│   ├── steps                         # Test steps implementation in python
│   ├── laytout.feature               # feature file that contains the scenario for checking User Interface controls
│   ├── operations.feature            # feature file that contains the scenarios for the arithmetic operations
│   ├── browser.py                    # Browser instance definition and configuration
│   ├── environment.py                # Defining the Tests Setup and Teardown methods

```

### Prerequisites

You need to have Python and virtualenv python package installed on your machine.
You will need also a browser webdriver downloaded to your machine.

### Running the Tests

1 - Clone this repository

2 - Change Directory to the project folder
```
 cd CalculatorTaskRF
```
3 - Activate the virutal environment using this command :
```
 source CalcTaskEnv/bin/activate
```
4 - Add the Chromedriver path to the virtualenv path variable using this command :
```
 export PATH=$PATH:/* your chromedriver path */
```
5 - Install nose python package using :
```
 pip install nose
```
You might get a permission denied exception, if so use sudo before the command and it should work.

6 - Change Directory to the Behave proejct folder :
```
 cd CalculatorBehave
```
7 - To Run tests :
```
 behave
```

### Defects Found

In the folder Defects you will find the full description of a UI defect detected with the technical information needed and a screenshot.
