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


.. _build-documentation:

Build the documentation
=======================

`Tox`_ is used for automating the build of the documentation. There are
different environments for cleaning the build, and building the documentation
in different formats such as HTML. , and running the tests. The following
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
