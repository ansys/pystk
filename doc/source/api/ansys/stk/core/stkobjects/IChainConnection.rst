IChainConnection
================

.. py:class:: IChainConnection

   object
   
   Provide access to a Chain connection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~from_object`
            * - :py:meth:`~to_object`
            * - :py:meth:`~min_num_uses`
            * - :py:meth:`~max_num_uses`
            * - :py:meth:`~parent_platform_restriction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainConnection


Property detail
---------------

.. py:property:: from_object
    :canonical: ansys.stk.core.stkobjects.IChainConnection.from_object
    :type: "IAgStkObject"

    From object for a connection.

.. py:property:: to_object
    :canonical: ansys.stk.core.stkobjects.IChainConnection.to_object
    :type: "IAgStkObject"

    To object for a connection.

.. py:property:: min_num_uses
    :canonical: ansys.stk.core.stkobjects.IChainConnection.min_num_uses
    :type: int

    Gets or sets the minimum number of uses for a connection.

.. py:property:: max_num_uses
    :canonical: ansys.stk.core.stkobjects.IChainConnection.max_num_uses
    :type: int

    Gets or sets the maximum number of uses for a connection.

.. py:property:: parent_platform_restriction
    :canonical: ansys.stk.core.stkobjects.IChainConnection.parent_platform_restriction
    :type: "CHAIN_PARENT_PLATFORM_RESTRICTION"

    Gets or sets the parent platform restriction for a connection.


