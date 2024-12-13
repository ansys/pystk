ChainConnection
===============

.. py:class:: ansys.stk.core.stkobjects.ChainConnection

   Class defining Chain connections.

.. py:currentmodule:: ChainConnection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.from_object`
              - From object for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.to_object`
              - To object for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.min_num_uses`
              - Gets or sets the minimum number of uses for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.max_num_uses`
              - Gets or sets the maximum number of uses for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.parent_platform_restriction`
              - Gets or sets the parent platform restriction for a connection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainConnection


Property detail
---------------

.. py:property:: from_object
    :canonical: ansys.stk.core.stkobjects.ChainConnection.from_object
    :type: IStkObject

    From object for a connection.

.. py:property:: to_object
    :canonical: ansys.stk.core.stkobjects.ChainConnection.to_object
    :type: IStkObject

    To object for a connection.

.. py:property:: min_num_uses
    :canonical: ansys.stk.core.stkobjects.ChainConnection.min_num_uses
    :type: int

    Gets or sets the minimum number of uses for a connection.

.. py:property:: max_num_uses
    :canonical: ansys.stk.core.stkobjects.ChainConnection.max_num_uses
    :type: int

    Gets or sets the maximum number of uses for a connection.

.. py:property:: parent_platform_restriction
    :canonical: ansys.stk.core.stkobjects.ChainConnection.parent_platform_restriction
    :type: ChainParentPlatformRestriction

    Gets or sets the parent platform restriction for a connection.


