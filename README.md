# Intro to pytest

## Important Commands

### Running all tests

`python -m pytest`

### Max fail

`python -m pytest --maxfail=1`

### Generate Report test 

* Using junit-xml 
`python -m pytest --junit-xml report.xml`

* Using html plugin
`python3 -m pytest --html=report.html`

### API/Feature/Integration Testes

`python -m pytest -m rest_api`

### Code Coverage

`python3 -m pytest --cov=stuff`
`python -m pytest --cov=stuff --cov=test`

*Adding Code coverage on html report*
`python3 -m pytest --cov=stuff --cov-report html`

## Plugins

* Html Report - pytest-html

`pip install pytest-html`

* pytest-cov and coverage.py

`pip install pytest-cov`

* pytest-xdist - run pytest tests in parallel (This is okay for small test suites but it can become very slow for large test suites)

`pip install pytest-xdist`

* pytest-bdd (Behavior-Driven Development)
