IAdvancedFixedWingGeometryVariable
==================================

.. py:class:: IAdvancedFixedWingGeometryVariable

   object
   
   Interface used to access the options for a variable geometry wing in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_aspect_ratio`
              - Set the aspect ratio of the aircraft.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aspect_ratio`
            * - :py:meth:`~start_sweep_mach`
            * - :py:meth:`~stop_sweep_mach`
            * - :py:meth:`~min_sweep_angle`
            * - :py:meth:`~max_sweep_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingGeometryVariable


Property detail
---------------

.. py:property:: aspect_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryVariable.aspect_ratio
    :type: float

    Get the aspect ratio of the aircraft.

.. py:property:: start_sweep_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryVariable.start_sweep_mach
    :type: float

    Gets or sets the mach number at which the wings start to sweep from the min sweep angle.

.. py:property:: stop_sweep_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryVariable.stop_sweep_mach
    :type: float

    Gets or sets the mach number at which the wings are swept to the max sweep angle.

.. py:property:: min_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryVariable.min_sweep_angle
    :type: typing.Any

    Gets or sets the minimum sweep angle of the wings.

.. py:property:: max_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometryVariable.max_sweep_angle
    :type: typing.Any

    Gets or sets the maximum sweep angle of the wings.


Method detail
-------------


.. py:method:: set_aspect_ratio(self, aspectRatio:float) -> None

    Set the aspect ratio of the aircraft.

    :Parameters:

    **aspectRatio** : :obj:`~float`

    :Returns:

        :obj:`~None`









