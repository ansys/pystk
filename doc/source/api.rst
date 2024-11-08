API reference
=============

This page contains the ``ansys-stk-core`` API reference.

.. jinja:: main_toctree

    {% if build_api %}

    .. toctree::
       :titlesonly:
    
       api/ansys/stk/core

    {% else %}

    .. warning::

        Set ``BUILD_API`` to ``true`` in your environment to build the API
        reference.

    {% endif %}
