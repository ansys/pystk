IAircraftSimpleProp
===================

.. py:class:: IAircraftSimpleProp

   object
   
   Interface used to access the Simple Propulsion options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_thrust_accel`
            * - :py:meth:`~min_thrust_decel`
            * - :py:meth:`~use_density_scaling`
            * - :py:meth:`~density_ratio_exponent`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftSimpleProp


Property detail
---------------

.. py:property:: max_thrust_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleProp.max_thrust_accel
    :type: float

    Gets or sets the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_decel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleProp.min_thrust_decel
    :type: float

    Gets or sets the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleProp.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftSimpleProp.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------







.. py:method:: set_density_scaling(self, useScaling:bool, exponent:float) -> None

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

    **useScaling** : :obj:`~bool`
    **exponent** : :obj:`~float`

    :Returns:

        :obj:`~None`

