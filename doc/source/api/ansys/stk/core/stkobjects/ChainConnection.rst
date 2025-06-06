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
              - Get or set the minimum number of uses for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.max_num_uses`
              - Get or set the maximum number of uses for a connection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnection.parent_platform_restriction`
              - Get or set the parent platform restriction for a connection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainConnection


Property detail
---------------

.. py:property:: from_object
    :canonical: ansys.stk.core.stkobjects.ChainConnection.from_object
    :type: ISTKObject

    From object for a connection.

.. py:property:: to_object
    :canonical: ansys.stk.core.stkobjects.ChainConnection.to_object
    :type: ISTKObject

    To object for a connection.

.. py:property:: min_num_uses
    :canonical: ansys.stk.core.stkobjects.ChainConnection.min_num_uses
    :type: int

    Get or set the minimum number of uses for a connection.

.. py:property:: max_num_uses
    :canonical: ansys.stk.core.stkobjects.ChainConnection.max_num_uses
    :type: int

    Get or set the maximum number of uses for a connection.

.. py:property:: parent_platform_restriction
    :canonical: ansys.stk.core.stkobjects.ChainConnection.parent_platform_restriction
    :type: ChainParentPlatformRestriction

    Get or set the parent platform restriction for a connection.


