Contributing as a developer
###########################

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`code-fork` Fork the repository
        :padding: 2 2 2 2
        :link: fork-the-repository
        :link-type: ref

        Learn how to fork the project and get your own copy.

    .. grid-item-card:: :fa:`download` Clone the repository
        :padding: 2 2 2 2
        :link: clone-the-repository
        :link-type: ref

        Download your own copy in your local machine.

    .. grid-item-card:: :fa:`download` Install for developers
        :padding: 2 2 2 2
        :link: install-for-developers
        :link-type: ref

        Install the project in editable mode.

    .. grid-item-card:: :fab:`docker` Build Docker containers
        :padding: 2 2 2 2
        :link: build-docker-containers
        :link-type: ref

        Build Docker containers for testing.

    .. grid-item-card:: :fa:`vial-circle-check` Run the tests
        :padding: 2 2 2 2
        :link: run-tests
        :link-type: ref

        Verify your changes by testing the project.

    .. grid-item-card:: :fa:`arrows-spin` Run the CI/CD pipelines
        :padding: 2 2 2 2
        :link: run-pipelines
        :link-type: ref

        Understand the different CI/CD pipelines.


.. _fork-the-repository:

Fork the repository
===================

Forking the repository is the first step to contributing to the project. This
allows you to have your own copy of the project so you can make changes without
affection the main project. Once you have made your changes, you can submit a
pull-request to the main project to have your changes reviewed and merged.

.. button-link:: https://github.com/ansys-internal/pystk/fork
    :color: primary
    :align: center

    :fa:`code-fork` Fork this project

.. note::

    If you are an Ansys employee, you can skip this step.

.. _clone-the-repository:

Clone the repository
====================

Make sure you `configure SSH <Connection to GitHub with SSH>`_ with your GitHub
account. This allows you to clone the repository without having to use tokens
or passwords. Also, make sure you have `git`_ installed in your machine.

To clone the repository, run:

.. code-block:: bash

    git clone git@github.com:ansys-internal/pystk

Finally, navigate to the project's root directory:

.. code-block:: text

    cd pystk

.. _install-for-developers:

Install for developers
======================

Installing PySTK in development mode allows you to perform changes to the code
and see the changes reflected in your environment without having to reinstall
the library every time you make a change.

Virtual environment
-------------------

Create a new virtual environment named ``.venv`` to isolate your system's
Python environment by running:

.. code-block:: text

    python -m venv .venv

Then, activate this environment by running:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    .venv\Scripts\activate.bat

            .. tab-item:: PowerShell

                .. code-block:: text

                    .venv\Scripts\Activate.ps1

    .. tab-item:: macOS/Linux/UNIX

        .. code-block:: text

            source .venv/bin/activate

Development mode
----------------

Install PySTK in editable mode by running:

.. code-block:: text

    python -m pip install --editable .

Verify the installation by checking the version of the library:


.. code-block:: python

    from ansys.stk.core import __version__


    print(f"PySTK version is {__version__}")

.. jinja::

    .. code-block:: text

       >>> PySTK version is {{ PYSTK_VERSION }}

Installing Tox
--------------

Once the project is installed, you can install `Tox`_. This is a cross-platform
automation tool. The main advantage of Tox is that it allows you to test your
project in different environments and configurations in a temporary and
isolated Python virtual environment. To install Tox, run:

.. code-block:: text

    python -m pip install tox

Finally, verify the installation by listing all the different environments
(automation rules) for PySTK:

.. code-block:: text

    python -m tox list

.. jinja:: toxenvs

    .. dropdown:: Default Tox environments
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Description
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            * - {{ name }}
              - {{ description }}
            {% endfor %}

.. _build-docker-containers:

Build Docker containers
=======================

STK is containerized using Docker. This allows you to deploy the project in
multiple environments without having to worry about dependencies.

.. _run-tests:

Run tests
=========

Once you have made your changes, you can run the tests to verify that your
modifications did not break the project. PySTK tests support different markers
to avoid running the whole suite of tests. These markers are associated to a
dedicated `Tox`_ environment.

.. jinja:: toxenvs

    .. dropdown:: Testing environments
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Command
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            {% if name.startswith("tests-")%}
            * - {{ name }}
              - python -m tox -e {{ name }}
            {% endif %}
            {% endfor %}


.. _run-pipelines:

Run CI/CD pipelines
===================
