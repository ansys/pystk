AccessTime
==========

.. py:class:: ansys.stk.core.stkobjects.AccessTime

   Bases: 

   Class for defining Sensor target times in terms of access.

.. py:currentmodule:: AccessTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTime.start_time`
              - Start time for the access period. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTime.stop_time`
              - Stop time for the access period. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTime.target`
              - Object to which there is access.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessTime


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.AccessTime.start_time
    :type: typing.Any

    Start time for the access period. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.AccessTime.stop_time
    :type: typing.Any

    Stop time for the access period. Uses DateFormat Dimension.

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.AccessTime.target
    :type: str

    Object to which there is access.


