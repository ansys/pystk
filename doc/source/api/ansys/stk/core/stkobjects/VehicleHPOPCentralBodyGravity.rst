VehicleHPOPCentralBodyGravity
=============================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity

   Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

.. py:currentmodule:: VehicleHPOPCentralBodyGravity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.set_maximum_degree_and_order`
              - Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.file`
              - Name of gravity (.grv) file, an ASCII file containing the Central Body geopotential model coefficients.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.max_degree`
              - Maximum degree of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.max_order`
              - Maximum order of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.use_ocean_tides`
              - Opt whether to include the perturbation of the gravity field caused by the effects of ocean tides.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.solid_tide_type`
              - Solid Tide Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.use_secular_variations`
              - Opt whether to include or ignore secular variations defined by the gravity field model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPCentralBodyGravity


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.file
    :type: str

    Name of gravity (.grv) file, an ASCII file containing the Central Body geopotential model coefficients.

.. py:property:: max_degree
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.max_degree
    :type: int

    Maximum degree of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: max_order
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.max_order
    :type: int

    Maximum order of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: use_ocean_tides
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.use_ocean_tides
    :type: bool

    Opt whether to include the perturbation of the gravity field caused by the effects of ocean tides.

.. py:property:: solid_tide_type
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.solid_tide_type
    :type: SOLID_TIDE

    Solid Tide Type.

.. py:property:: use_secular_variations
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.use_secular_variations
    :type: bool

    Opt whether to include or ignore secular variations defined by the gravity field model.


Method detail
-------------













.. py:method:: set_maximum_degree_and_order(self, maximumDegree: int, maximumOrder: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity.set_maximum_degree_and_order

    Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    :Parameters:

    **maximumDegree** : :obj:`~int`
    **maximumOrder** : :obj:`~int`

    :Returns:

        :obj:`~None`

