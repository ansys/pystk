AdvancedFixedWingGeometryVariable
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometry`

   Class defining a variable geometry wing in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingGeometryVariable

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.set_aspect_ratio`
              - Set the aspect ratio of the aircraft.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.aspect_ratio`
              - Get the aspect ratio of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.max_sweep_angle`
              - Get or set the maximum sweep angle of the wings.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.min_sweep_angle`
              - Get or set the minimum sweep angle of the wings.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.start_sweep_mach`
              - Get or set the mach number at which the wings start to sweep from the min sweep angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.stop_sweep_mach`
              - Get or set the mach number at which the wings are swept to the max sweep angle.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingGeometryVariable


Property detail
---------------

.. py:property:: aspect_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.aspect_ratio
    :type: float

    Get the aspect ratio of the aircraft.

.. py:property:: max_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.max_sweep_angle
    :type: typing.Any

    Get or set the maximum sweep angle of the wings.

.. py:property:: min_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.min_sweep_angle
    :type: typing.Any

    Get or set the minimum sweep angle of the wings.

.. py:property:: start_sweep_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.start_sweep_mach
    :type: float

    Get or set the mach number at which the wings start to sweep from the min sweep angle.

.. py:property:: stop_sweep_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.stop_sweep_mach
    :type: float

    Get or set the mach number at which the wings are swept to the max sweep angle.


Method detail
-------------






.. py:method:: set_aspect_ratio(self, aspect_ratio: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable.set_aspect_ratio

    Set the aspect ratio of the aircraft.

    :Parameters:

        **aspect_ratio** : :obj:`~float`


    :Returns:

        :obj:`~None`





