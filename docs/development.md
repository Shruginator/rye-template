### Quick Navigation

- [Documentation Navigation](navigation.md)


# Development

- [Commit Messages](#commit-messages)
- [Rye](#rye)
- [Releases](#releases)
- [Update Readme Badges](#update-readme-badges)


## Commit Messages

### General Structure

The following structure is encouraged for commit messages:

1. **Title Line** (summary)  
    A single line starting with the acronym, followed by a brief but informative
    summary.  
    Example:
    ```
    ENH: Add bootstrapping method for confidence intervals
    ```

2. **Body** (optional but recommended)  
    A few sentences explaining what was changed and why.
    If relevant, mention the context or problem solved.
    Keep lines under 72 characters.  
    Example:
    ```
    Added a function to compute confidence intervals using the bootstrap method.
    This helps handle small sample sizes without assuming normality.
    ```

3. **Footer** (optional)  
    Include metadata like issue numbers, co-authors, or breaking changes.
    Example:
    ```
    Closes #42
    ```

### Commit Acronyms

Use the following acronyms to start your commit messages:

| Acronym | Use Case |
|-|-|
|API|An (incompatible) API change|
|BLD| Change related to building the library|
|FIX| Bug fix|
|DEP| Deprecate something, or remove a deprecated object|
|DEV| Development tool or utility|
|DOC| Documentation|
|ENH| Enhancement|
|MNT| Maintenance commit (refactoring, typos, etc.)|
|REV| Revert an earlier commit|
|STY| Style fix (whitespace, PEP8)|
|TST| Addition or modification of tests|
|REL| Related to releases|

The definitions are based on the acronyms recommended in the
[Numpy Development Workflow](#ref-numpy-commit-acronyms) of the popular Python library
[Numpy](https://github.com/numpy/numpy).

For example, `git commit -m "ENH: Add IQR-based outlier removal method"`.


## Rye

[Rye](https://rye.astral.sh/) is used to manage this project.
In particular, it is used to handle the Python installation, the virtual environment
(venv) and the build process.
Its installation instructions can be found on the website.

The following subsections contain a collection of useful commands grouped by category.

### Virtual Environment

|Command|Description|
|--|--|
|`rye sync`|Sync the venv with the dependencies listed in `pyproject.toml`.|
|`rye sync --update all`|Update all dependencies to their latest versions.|
|`rye add <lib_name>`|Add a dependency.|
|`rye add --dev <lib_name>`|Add a development dependency.
|`rye list`|List all installed dependencies.|
|`rye remove <lib_name>`|Remove a dependency.|
|`rye remove --dev <lib_name>`|Remove a development dependency.|


### Code Style

|Command|Description|
|--|--|
|`rye run ruff check --fix`| Lint with [Ruff](https://docs.astral.sh/ruff/) and automatically fix issues, when possible.|
|`rye lint --fix`|Shorter alias for the command above.|
|`rye check --fix`| Another alias for the command above.|
|`rye run ruff format .`|Format the code with Ruff and write back to the files.|
|`rye fmt`|Shorter alias for the command above.|
|`rye run mypy`|Validate the type hinting with [MyPy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).|


### Tests

|Command|Description|
|--|--|
|`rye run pytest`|Run the test suite via [Pytest](https://github.com/pytest-dev/pytest).|
|`rye test`|Shorter alias for the command above.|
|`rye run coverage run -m pytest`|Perform a test coverage analysis.|
|`rye run coverage report`|Generate a report.|
|`rye run coverage xml`|Generate an XML report for the coverage badge update. See section [Coverage Badge](#coverage-badge).|


If the test suite grows bigger and bigger, it might take significant time to run all the
tests.
Luckily, there are quick references to only run specific tests:

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


### Running Scripts

To run a script in the environment managed by Rye, it first must be defined in the
`pyproject.toml`.
For example:

```
[tool.rye.scripts]
main = { cmd = "python src/path/to/script.py" }
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


## Update Readme Badges

### Coverage Badge

The library [Genbadge](https://smarie.github.io/python-genbadge/) is used for the test
coverage badge.
In order to generate and update the badge, run the following sequence of
commands:

```zsh
# Run the test suite with coverage
rye run coverage run -m pytest

# Create XML summary file, which will be used to generate the badge
rye run coverage xml

# Generate the badge by providing input and output paths
rye run genbadge coverage -i badges/coverage.xml -o badges/coverage_badge.svg
```

### Python Version Badge

For the Python version badges in the readme file Google's open source library
[Pybadges](https://github.com/google/pybadges) is used.
The following command generates the badge for the desired Python versions, in this
example `>=3.12`:

```zsh
rye run python -m pybadges \
    --left-text="python" \
    --right-text=">=3.12" \
    --whole-link="https://www.python.org/" \
    --embed-logo="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/python.svg" \
    > badges/python_badge.svg
```


## Releases

### Release Versioning

The version number of the project can be found in the `pyproject.toml` under the section
`project.version`, usually right at the top of the file.

Following the popular [Semantic Versioning](#ref-semantic-versioning) for version
numbers, the version format should be `MAJOR.MINOR.PATCH` with the following rules for
number incrementing:

|Part|Increment Reason|
|--|--|
|MAJOR|Incompatible API changes.|
|MINOR|Addition of functionality in a backward compatible manner.|
|PATCH|Backward compatible bug fixes.|


### Release Notes

To create a release via GitHub simply use the release tool and add a description in the
following form:

```markdown
# [vX.Y.Z] - YYYY-MM-DD

## New Features

- List and describe any new feature
- ...

## Improvements

- ...

## Bug Fixes

- ...

## Breaking Changes

- ...

## Known Issues

- ...
```

Feel free to add the release notes autogenerated by GitHub below these notes.


## References

<!-- Text reference example: [[Numpy Development Workflow]](#ref-numpy-commit-acronyms) -->
<a id="ref-numpy-commit-acronyms">[Numpy Development Workflow]</a> 
NumPy Developers. 
*Development workflow*. 
Retrieved 10.03.2025,
from [numpy.org/doc/stable/dev/development_workflow.html](https://numpy.org/doc/stable/dev/development_workflow.html).

<a id="ref-semantic-versioning">[Semantic Versioning]</a> 
Tom Preston-Werner. 
*Semantic Versioning 2.0.0*. 
Retrieved 20.11.2024,
from [semver.org/spec/v2.0.0.html](https://semver.org/spec/v2.0.0.html).
