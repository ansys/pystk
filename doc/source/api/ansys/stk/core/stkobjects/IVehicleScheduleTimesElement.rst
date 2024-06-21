IVehicleScheduleTimesElement
============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleScheduleTimesElement

   object
   
   Parameters for scheduled times for target pointing attitude.

.. py:currentmodule:: IVehicleScheduleTimesElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.start`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.stop`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.target`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleScheduleTimesElement


Property detail
---------------

.. py:property:: start
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.start
    :type: typing.Any

    Start time. Uses DateFormat Dimension.

.. py:property:: stop
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.stop
    :type: typing.Any

    Stop time. Uses DateFormat Dimension.

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.IVehicleScheduleTimesElement.target
    :type: ILinkToObject

    Get the target.


