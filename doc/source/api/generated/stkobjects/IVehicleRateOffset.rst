IVehicleRateOffset
==================

.. py:class:: IVehicleRateOffset

   object
   
   Rate and offset interface for precession and spin.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~rate`
            * - :py:meth:`~offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRateOffset


Property detail
---------------

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.IVehicleRateOffset.rate
    :type: float

    Rate of precession or spin. Uses AngleRate Dimension.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.IVehicleRateOffset.offset
    :type: float

    Initial offset of precession. Uses Angle Dimension.


