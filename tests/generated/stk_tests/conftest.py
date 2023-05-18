from test_util import EngineLifetimeManager, CategoryManager


def pytest_addoption(parser):
    parser.addoption(
        "--target",
        action="store",
        dest="target",
        help="target application to run the tests with",
        default="StkXNoGfx",
        choices=["Stk", "StkX", "StkXNoGfx"],
    )

    parser.addoption(
        "--include",
        action="append",
        dest="included_categories",
        help="name of category to include, repeat option to include multiple categories",
        metavar="<category name>",
    )

    parser.addoption(
        "--exclude",
        action="append",
        dest="excluded_categories",
        help="name of category to exclude, repeat option to exclude multiple categories",
        metavar="<category name>",
    )


def pytest_sessionstart(session):
    target = session.config.getoption("--target")
    print(f"\nInitializing STK in {target} mode")
    EngineLifetimeManager.Initialize(lock=True, target=target)

    included_categories = session.config.getoption("--include")
    if included_categories is not None:
        print(f"Included categories: {','.join(included_categories)}")
        for category in included_categories:
            CategoryManager.AddIncludedCategory(category)

    excluded_categories = session.config.getoption("--exclude")
    if excluded_categories is not None:
        print(f"Excluded categories: {','.join(excluded_categories)}")
        for category in excluded_categories:
            CategoryManager.AddExcludedCategory(category)

    print()


def pytest_sessionfinish(session):
    print("\n\nUninitializing STK")
    EngineLifetimeManager.Uninitialize(force=True)
