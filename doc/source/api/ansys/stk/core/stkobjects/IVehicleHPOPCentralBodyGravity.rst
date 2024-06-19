IVehicleHPOPCentralBodyGravity
==============================

.. py:class:: IVehicleHPOPCentralBodyGravity

   object
   
   Central Body Gravity interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_maximum_degree_and_order`
              - Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~file`
            * - :py:meth:`~max_degree`
            * - :py:meth:`~max_order`
            * - :py:meth:`~use_ocean_tides`
            * - :py:meth:`~solid_tide_type`
            * - :py:meth:`~use_secular_variations`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPCentralBodyGravity


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.file
    :type: str

    Name of gravity (.grv) file, an ASCII file containing the Central Body geopotential model coefficients.

.. py:property:: max_degree
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.max_degree
    :type: int

    Maximum degree of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: max_order
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.max_order
    :type: int

    Maximum order of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: use_ocean_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.use_ocean_tides
    :type: bool

    Opt whether to include the perturbation of the gravity field caused by the effects of ocean tides.

.. py:property:: solid_tide_type
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.solid_tide_type
    :type: SOLID_TIDE

    Solid Tide Type.

.. py:property:: use_secular_variations
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.use_secular_variations
    :type: bool

    Opt whether to include or ignore secular variations defined by the gravity field model.


Method detail
-------------













.. py:method:: set_maximum_degree_and_order(self, maximumDegree: int, maximumOrder: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPCentralBodyGravity.set_maximum_degree_and_order

    Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    :Parameters:

    **maximumDegree** : :obj:`~int`
    **maximumOrder** : :obj:`~int`

    :Returns:

        :obj:`~None`

