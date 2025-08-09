HoverAltitudeOptions
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions

   Class defining the altitude options for a VTOL procedure.

.. py:currentmodule:: HoverAltitudeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.altitude_reference`
              - Get or set the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.altitude`
              - Get or set the altitude for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.final_altitude_rate`
              - Get or set the altitude rate of the aircraft at the end of the procedure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import HoverAltitudeOptions


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.altitude_reference
    :type: AGLMSL

    Get or set the altitude reference.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.altitude
    :type: float

    Get or set the altitude for the procedure.

.. py:property:: final_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions.final_altitude_rate
    :type: VTOLRateMode

    Get or set the altitude rate of the aircraft at the end of the procedure.


