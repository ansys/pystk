"""The API migration assistant applies code transformations to upgrade code to a new version of an API."""

import sys
from .api_migration_assistant import main

if __name__ == "__main__":
    sys.exit(main())
