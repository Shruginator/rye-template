### Quick Navigation

- [Documentation Navigation](navigation.md)


# Development

- [Commit Acronyms](#commit-acronyms)
- [Rye](#rye)
- [Releases](#releases)
- [Readme Badges Update](#readme-badges-update)


## Commit Acronyms

Comming soon.


## Rye

[Rye](https://rye.astral.sh/) is used to manage this project, in particular, the Python
installation, the virtual environment (venv) handling and the build process.
Its installation instructions can be found on the website.

It follows a collection of useful commands.

### Virtual Environment

|Command|Description|
|--|--|
|`rye sync`|Sync the venv with the dependencies listed in `pyproject.toml`.|
|`rye sync --update all`|Update all dependencies to their latest versions.|
|`rye add <lib_name>`|Add a dependency.|
|`rye add --dev <lib_name>`|Add a development dependency.
|`rye list`|List all installed dependencies.|
|`rye remove`|Remove a dependency.|


### Code Style

|Command|Description|
|--|--|
|`rye run ruff check --fix`| Lint with [Ruff](https://docs.astral.sh/ruff/) and automatically fix issues, when possible.|
|`rye lint --fix`|Shorter alias for the command above.|
|`rye run ruff format .`|Format the code with Ruff and write back to the files.|
|`rye fmt`|Shorter alias for the command above.|
|`rye run mypy`|Validate the type hinting with [MyPy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).|


### Tests

|Command|Description|
|--|--|
|`rye run -m pytest`|Run the test suite via `Pytest`.|
|`rye test`|Shorter alias for the command above.|
|`rye run coverage run -m pytest`|Perform a test coverage analysis.|
|`rye run coverage report`|Generate a report.|
|`rye run coverage xml`|Generate an `xml` report for the coverage badge update. See section [Coverage Badge](#coverage-badge).|


If the test suite grows bigger and bigger, it might take significant time to run all the
tests.
Therefore, here some quick reference examples to only run specific tests:

```sh
# Select test file
rye run pytest -k "example_test.py"  # Keyword w/ file name
rye run pytest tests/example_test.py  # File name

# Select test class
rye run pytest -k "TestHelloWorld"  # Keyword w/ class name
rye run pytest tests/example_test.py::TestHelloWorld  # File and class name

# Select test function
rye run pytest -k "test_return"  # Keyword w/ function name
rye run pytest tests/example_test.py::test_return  # File and function name

# Select test function more specifically
rye run pytest tests/example_test.py::TestHelloWorld::test_return  # File, class and function name
```


### Running Scrips

To run a script in the environment managed by Rye, it first must be defined in the
`pyproject.toml`.
For example:

```
[tool.rye.scripts]
main = { cmd = "python src/vwg_mem/main.py" }
```

Then it can be run as follows:

```
rye run main
```

### Build

|Command|Description|
|--|--|
|`rye build`|Build the sdist and wheel targets in the `dist` target.|
|`rye build --clean`|Remove older builds from the build directory before building.|


## Releases

### Release Versioning

Following the popular [[Semantic Versioning]](#ref-semantic-versioning) for version
numbers, the version format should be `MARJOR.MINOR.PATCH` with the following rules for
number incrementing:

|Part|Increment Reason|
|--|--|
|MAJOR|Incompatible API changes.|
|MINOR|Addition of functionality in a backward compatible manner.|
|PATCH|Backward compatible bug fixes.|


## Readme Badges Update


### Coverage Badge

For the test coverage badge we use the
[Genbadge](https://smarie.github.io/python-genbadge/) library.
In order to generate and update the coverage badge, run the following sequence of
commands after `rye run coverage run -m pytest`:

```zsh
# Create XML summary file, which will be used to generate the badge
rye run coverage xml

# Generate the badge by providing input and output paths
rye run genbadge coverage -i badges/coverage.xml -o badges/coverage_badge.svg
```

### Python Version Badge

For the Python version badges in the readme file we use Google's open source
[Pybadges](https://github.com/google/pybadges).
The following command generates the badge for the desired Python versions:

```zsh
rye run python -m pybadges \
    --left-text="python" \
    --right-text=">=3.12" \
    --whole-link="https://www.python.org/" \
    --embed-logo="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/python.svg" \
    > badges/python_badge.svg
```


## References

<a id="ref-semantic-versioning">[Semantic Versioning]</a> 
Tom Preston-Werner. 
*Semantic Versioning 2.0.0*. 
Retrieved 20.11.2024,
from semver.org/spec/v2.0.0.html.
