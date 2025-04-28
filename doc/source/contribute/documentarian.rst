Contributing as a documentarian
###############################

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`pencil` Write documentation
        :padding: 2 2 2 2
        :link: write-documentation
        :link-type: ref

        Explain how to get started, use, and contribute to the project.

    .. grid-item-card:: :fa:`laptop-code` Add a new example
        :padding: 2 2 2 2
        :link: write-examples
        :link-type: ref

        Showcase the capabilities of PySTK by adding a new example. 

    .. grid-item-card:: :fa:`clone` Add a new code snippet
        :padding: 2 2 2 2
        :link: write-snippets
        :link-type: ref

        Demonstrate a common PySTK task by adding a new code snippet.

    .. grid-item-card:: :fa:`file-code` Build the documentation
        :padding: 2 2 2 2
        :link: build-documentation
        :link-type: ref

        Render the documentation to see your changes reflected.

.. _write-documentation:

Write documentation
===================

The documentation generator used in PySTK is `Sphinx`_. Most of the documents
are written in `reStructuredText`_. Some parts of the documentation, like the
:ref:`examples <Examples>`, use mix of `markdown`_ and Python. If
you are interested in writing examples, see the :ref:`writing examples <write-examples>` 
section.

The documentation is located in the ``doc/source`` directory. The landing page
is declared in the ``doc/source/index.rst`` file. The rest of the files contain
the main pages of different sections of the documentation. Finally, the
``doc/source/_static/`` folder contains various assets like images, and CSS
files.

The layout of the ``doc/source`` directory is reflected in the slug of the
online documentation. For example, the
``doc/source/contribute/documentarian.rst`` renders as
``https://docs.pystk.com/contribute/documentarian``. 

Thus, if you create a new file, it important to follow these rules:

- Use lowercase letters for file and directory names
- Use short and descriptive names
- Use hyphens to separate words
- Play smart with the hierarchy of the files and directories

All files need to be included in a table of contents. No dangling files are
permitted. If a file is not included in the table of contents, Sphinx raises a
warning that makes the build to fail.

A table of contents can be declared using a directive like this:

.. code-block:: rst

    .. toctree::
        :hidden:
        :maxdepth: 3

        path-to-file-A
        path-to-file-B
        path-to-file-C
        ...

The path to the file is relative to the directory where the table of contents
is declared.

.. _write-examples:

Write a new example
===================

The :ref:`examples <Examples>` section of the documentation showcases different
capabilities of PySTK. Each example is a standalone Python script. Despite
being ``*.py`` files, they are written in a mix of `markdown`_ and Python. This
is possible thanks to the `myst-parser`_ Sphinx extension. In addition, these
Python files can be opened as Jupyter Notebooks thanks to the `jupytext`_
extension.

Documentarians writing new examples are encouraged to open a new Jupyter Lab
session and write the example as a Jupyter Notebook. This way, the
documentarian can test the code and see the output in real-time. The created
Jupyter Notebook gets stored as a Python file automatically.

Finally, here are some tips for writing examples:

- Start the example with an explanation of the main topic. For example, if you
  are discussing a certain orbital maneuver, explain what that maneuver
  entails. Similarly, if an example is centered around satellite coverage,
  provide an explanation of what coverage is. Try to use as many relevant
  keywords as possible in this section to optimize for Search Engine
  Optimization.

- The second section of the example should be a problem statement. This
  statement should include all of the parameters needed in the example, as well
  as a description of what the example aims to determine. Write this section in
  an imperative form.

- Include an explanation with each code cell. In a Jupyter notebook, this
  entails adding a markdown cell before each code cell. The explanations should
  be included before, not after, the corresponding code.

- The examples are built with the documentation and included in the help. As
  part of the build process, screenshots of the STK Engine 2D and 3D graphics
  are inserted in the document. You do not need to include the screenshots
  yourself. However, do include the graphics widgets (2D or 3D) at points in
  your example. When the documentation is built, a screenshot of the widget
  is inserted in its place. Jupyter widgets are included in
  :py:mod:`~ansys.stk.core.stkengine.experimental.jupyterwidgets`.

.. _write-snippets:

Write a new code snippet
========================

The :ref:`code snippets <PySTK code snippets>` demonstrate how to perform
common tasks in PySTK. Code snippets are written in `pytest`_ test functions 
in the `code snippet directory`_ and are run as part of the 
tests. They are also included in the documentation, providing PySTK users 
useful templates for the building blocks of PySTK scenario design. This 
enables the snippets to appear:

- On the API reference pages for the elements used in the snippet
- On the :ref:`code snippets <PySTK code snippets>` landing page
- In the quick info provided by code completion tools such as `IntelliSense`_

To contribute your own code snippet, first identify the critical API element 
or elements used in the snippet. In the following example, the primary element 
of interest is the :py:class:`~ansys.stk.core.stkobjects.Scenario` object. 
Additionally, for instructional purposes, this example demonstrates the 
process of attaching this snippet to its
:py:meth:`~ansys.stk.core.stkobjects.Scenario.set_time_period()` method.

.. literalinclude:: /../../tests/doc_snippets_tests/scenario/scenario_management/scenario_management_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def SetScenarioTimePeriodSnippet
  :end-at: # Use scenario.start_time, scenario.stop_time to get time period
  :dedent:

Next, wrap the snippet in a method with a descriptive name ending with 
``Snippet``. If the method consumes a non-self parameter, add a comment to the 
first line of the method describing its type to orient the user to the 
snippet's assumed configuration. Decorate this method with PySTK's 
``@code_snippet`` decorator:

.. list-table::
    :header-rows: 1
    :widths: auto
    
    * - **Attribute**
      - **Description**
    * - **name**
      - A Pascal-cased name briefly describing the snippet's objective (tip: use this name followed by ``Snippet`` to name the function enclosing the snippet)
    * - **description**
      - A sentence-style phrase describing the task performed in the snippet
    * - **category**
      - A ``|``-separated list describing the organization of the capability. See the :ref:`code snippets <PySTK code snippets>` landing page for the list of existing categories and subcategories. New categories can be created on a need basis.
    * - **eid**
      - A ``|``-separated list of ids for the one or more elements previously identified as central to the snippet. Each id should be of the form ``<module>~<class/interface name>(~<method/property name>)`` where ``module`` represents the namespace of the module where the element is defined, starting after ``ansys.stk.core``. Omit the parenthesized portion if the ``eid`` corresponds to a class or interface.

Here is an example of a decorated method for the preceding code snippet:

.. literalinclude:: /../../tests/doc_snippets_tests/scenario/scenario_management/scenario_management_snippets.py
  :language: py
  :tab-width: 4
  :prepend: @code_snippet(
  :start-after: name="SetScenarioTimePeriod",
  :end-at: # Use scenario.start_time, scenario.stop_time to get time period
  :dedent:

Next, add a pytest-discoverable method (beginning with ``test``) that calls
the decorated method. This new method should perform any configuration that 
the decorated method assumes upon entry. When automating this configuration, 
you may assume that an STK application is started and a basic STK scenario is 
open. You may access the :py:class:`~ansys.stk.core.stkobjects.StkObjectRoot`
for this application using ``self.get_root()``.

.. literalinclude:: /../../tests/doc_snippets_tests/scenario/scenario_management/scenario_management_snippets.py
  :language: py
  :tab-width: 4
  :start-at: def test_SetScenarioTimePeriodSnippet
  :end-at: # Use scenario.start_time, scenario.stop_time to get time period
  :dedent:

Copy these methods into the file corresponding to the value provided for the 
``@code_snippet`` decorator's ``category`` attribute. 

.. note:: 

    If you created a new category for this attribute, you may also need to 
    create a new test file. If this is the case, create a copy of 
    ``template_snippets.py`` in the `code snippet directory`_ and rename the copy 
    ``<subcategory>_snippets.py`` where ``<subcategory>`` is the new subcategory. 
    If necessary, create directories matching the category organization up to 
    ``doc_snippets_tests``.

Run the tests defined in the `code snippet directory`_ and make sure 
your new snippet runs and passes.

.. vale off

.. code-block:: console

   $ python -m tox -e test-snippets

.. vale on

To ensure properly formatted changes (including additions, deletions, and 
modifications) to the snippets in the `code snippet directory`_ are 
propagated to the corresponding documentation and source files, PySTK provides 
a snippet updater tool.

.. vale off

.. code-block:: console

   $ python -m tox -e doc-snippets

.. vale on

View the changes using a diff application to ensure the process completed 
smoothly. Once you have verified these changes, you are ready to open a PR on
the `PySTK pull requests`_ page.

.. _build-documentation:

Build the documentation
=======================

`Tox`_ is used for automating the build of the documentation. There are
different environments for cleaning the build, running the tests, and building
the documentation in different formats such as HTML or PDF. The following
environments are available:

The following
environments are available:

.. jinja:: toxenvs

    .. dropdown:: Documentation environments
        :animate: fade-in
        :icon: three-bars

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Environment
              - Command
            {% for environment in envs %}
            {% set name, description  = environment.split("->") %}
            {% if name.startswith("doc-")%}
            * - {{ name }}
              - python -m tox -e {{ name }}
            {% endif %}
            {% endfor %}

Two environment variables are available for the documentation build:

- ``BUILD_EXAMPLES``: if set to ``true``, the examples are built. This is the
  default behavior. When set to ``false``, the examples are not built.

- ``BUILD_API``: if set to ``true``, the API documentation is built. This is
  the default behavior. When set to ``false``, the API documentation is not
  built.

By using these environment variables, you can speed up the build process. This
allows to shorten the build time when only certain parts of the documentation
are modified.
