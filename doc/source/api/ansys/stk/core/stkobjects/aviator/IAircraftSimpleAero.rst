IAircraftSimpleAero
===================

.. py:class:: IAircraftSimpleAero

   object
   
   Interface used to access the Simple Aerodynamics options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~operating_mode`
            * - :py:meth:`~s_reference`
            * - :py:meth:`~cl_max`
            * - :py:meth:`~cd`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftSimpleAero


Property detail
---------------

.. py:property:: operating_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleAero.operating_mode
    :type: AERO_PROP_SIMPLE_MODE

    Gets or sets the mode option to treat the aircraft as a helicopter or a fixed wing aircraft when calculating the aircraft's attitude.

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleAero.s_reference
    :type: float

    Gets or sets the reference surface area of the aircraft.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleAero.cl_max
    :type: float

    Gets or sets the max coefficient of lift.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleAero.cd
    :type: float

    Gets or sets the coefficient of drag.


