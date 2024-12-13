AircraftSimpleAerodynamic
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic

   Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftSimpleAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.operating_mode`
              - Gets or sets the mode option to treat the aircraft as a helicopter or a fixed wing aircraft when calculating the aircraft's attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.s_reference`
              - Gets or sets the reference surface area of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cl_max`
              - Gets or sets the max coefficient of lift.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cd`
              - Gets or sets the coefficient of drag.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftSimpleAerodynamic


Property detail
---------------

.. py:property:: operating_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.operating_mode
    :type: AerodynamicPropulsionSimpleMode

    Gets or sets the mode option to treat the aircraft as a helicopter or a fixed wing aircraft when calculating the aircraft's attitude.

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.s_reference
    :type: float

    Gets or sets the reference surface area of the aircraft.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cl_max
    :type: float

    Gets or sets the max coefficient of lift.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cd
    :type: float

    Gets or sets the coefficient of drag.


