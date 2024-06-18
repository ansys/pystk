IAccessTime
===========

.. py:class:: IAccessTime

   object
   
   IAgAccessTime Interface, part of the target times scheme for specifying when a satellite or sensor can access a given object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~target`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessTime


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IAccessTime.start_time
    :type: typing.Any

    Start time for the access period. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IAccessTime.stop_time
    :type: typing.Any

    Stop time for the access period. Uses DateFormat Dimension.

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.IAccessTime.target
    :type: str

    Object to which there is access.


