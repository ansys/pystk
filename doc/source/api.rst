API reference
=============

This page contains the API reference for the ``ansys-stk-core`` and
``ansys-stk-extensions`` libraries.

.. jinja:: main_toctree

    {% if build_api %}

    .. toctree::
       :titlesonly:
    
       api/ansys/stk/core
       api/ansys/stk/extensions

    {% else %}

    .. warning::

        Set ``BUILD_API`` to ``true`` in your environment to build the API
        reference.

    {% endif %}
