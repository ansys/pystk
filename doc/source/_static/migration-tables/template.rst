{{ module }}
The ``agi.stk.graphics`` module
===============================

{% if interfaces %}
Interfaces
----------

{% for interface in interfaces %}

{{ interface.name }}
{{ '^' * len(interface.name) }}

The new name is :py:class:`~{{ module }}.{{ interface }}`.

{% if interface.properties or instance.methods %}
.. tab-set::

    {% if interface.properties %}
    .. tab-item:: Properties

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Old name
              - New name
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngine.start_application`
              - :py:attr:`~ansys.stk.core.stkengine.STKEngine.start_application`
    {% endif %}

    {% if interface.properties %}
    .. tab-item:: Methods

        .. list-table::
            :header-rows: 1
            :widths: auto

            * - Old name
              - New name
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngine.start_application`
              - :py:attr:`~ansys.stk.core.stkengine.STKEngine.start_application`

    {% endif %}

{% endif %}
{% endif %}
