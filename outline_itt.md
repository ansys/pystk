Time allocation
- 10 minutes introduction
- 50 minutes workshop

Prerequesites
- STK 12.10
- Python 3.11 or greater
- GitHub account enabled for ansys-internal access
- git, GitHub Desktop recommended

(before the meeting download wheels and doc to make available on AGI network)

Introduction
- Open sourcing PySTK in the next few weeks
- Status update
- Looking for feedback

Workshop
- End-user / consumer perspective (means access to the doc, but not cloning the repo)
    - Walk through online documentation at https://stk.docs.pyansys.com/
        - Highlight part of PyAnsys ecosystem and show other PyAnsys docs
    - Show to download artifact from https://stk.docs.pyansys.com/version/dev/artifacts.html
        - Explain required artifacts and extra wheelhouses
    - Create and activate virtual environment
    - Install PySTK wheel and extra wheelhouses if applicable
    - Create hello STK script
        - explain desktop vs engine vs runtime
    - Highlight code completion
    - Migrate an existing Python file using current STK Python API
        - Extract CodeSamples\Automation\Python\STKProTutorial.py "C:\Program Files\AGI\STK 12\CodeSamples\CodeSamples.zip"
        - Install current API wheel from "C:\Program Files\AGI\STK 12\bin\AgPythonAPI\agi.stk12-12.10.0-py3-none-any.whl"   
        - Run before migration
        - Use api-migration-assistant to migrate to PySTK
        - Run resulting app
        - Diff and validate
    - How to create jupyter notebook with visualization
    - Looking at code snippets and examples in the help
        - Run one of the examples in jupyter lab
- Contributor perspective
    - GitHub overview
        - How to submit a GitHub issues
        - How to create a Pull Request
            - CI/CD checks
            - Code style
    - Tox and tooling
    - Contributing documentation
        - Doc style checks
    - Contributing an example
    - Contributing code snippets
    - Docker usage overview
- Wrap up
    - Please provide feedback!
    - Plug for Teams channel



