IHoverAltitudeOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions

   object
   
   Interface used to access the altitude options for VTOL procedure.

.. py:currentmodule:: IHoverAltitudeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.altitude_reference`
              - Gets or sets the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.altitude`
              - Gets or sets the altitude for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.final_altitude_rate`
              - Gets or sets the altitude rate of the aircraft at the end of the procedure.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IHoverAltitudeOptions


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.altitude_reference
    :type: AGL_MSL

    Gets or sets the altitude reference.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.altitude
    :type: float

    Gets or sets the altitude for the procedure.

.. py:property:: final_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IHoverAltitudeOptions.final_altitude_rate
    :type: VTOL_RATE_MODE

    Gets or sets the altitude rate of the aircraft at the end of the procedure.


