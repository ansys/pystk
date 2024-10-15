Contributing as a documentarian
###############################

.. grid:: 1 1 3 3

    .. grid-item-card:: :fa:`pencil` Write documentation
        :padding: 2 2 2 2
        :link: write-documentation
        :link-type: ref

        Explain others how to get started, use, and contribute to the project.

    .. grid-item-card:: :fa:`laptop-code` Add a new example
        :padding: 2 2 2 2
        :link: write-examples
        :link-type: ref

        Showcase the capabilities of PySTK by adding a new example. 

    .. grid-item-card:: :fa:`search` Focus on SEO
        :padding: 2 2 2 2
        :link: focus-on-seo
        :link-type: ref

        Ensure that the documentation is easily discoverable.


.. _write-documentation:

Write documentation
===================

The documentation generator used in PySTK is `Sphinx`_. Most of the documents
are written in `reStructuredText`_. Some parts of the documentation, like the
:ref:`examples <Examples>`, use mix of `markdown`_ and Python. If
you are interested in writing examples, see the :ref:`writing examples <Writing
examples>` section.

The documentation is located in the ``doc/source`` directory. The landing page
is declared in the ``doc/source/index.rst`` file. The rest of the files contain
the main pages of different sections of the documentation. Finally, the
``doc/source/_static/`` folder contains various assets like images, and CSS
files.

The layout of the ``doc/source`` directory is reflected in the slug of the
online documentation. For example, the
``doc/source/contribute/documentarian.rst`` will render as
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

