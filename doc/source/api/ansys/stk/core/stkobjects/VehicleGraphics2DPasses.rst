VehicleGraphics2DPasses
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DPasses

   Settings for satellite pass display graphics.

.. py:currentmodule:: VehicleGraphics2DPasses

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.set_pass_type`
              - Pass display option: show all or those in a user-specified range.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.is_pass_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.pass_type`
              - Pass display option: show all or those in a user-specified range.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.pass_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.satellite_pass`
              - Get the pass property.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.visible_sides`
              - Gets or sets the visible sides option for the pass: ascending, descending, both or none.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.show_pass_labels`
              - Opt whether to display pass numbers at the pass break locations in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses.show_path_labels`
              - Opt whether to display path numbers within a repeating ground track sequence at the pass break locations in the 2D Graphics window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DPasses


Property detail
---------------

.. py:property:: pass_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.pass_type
    :type: VehicleGraphics2DPass

    Pass display option: show all or those in a user-specified range.

.. py:property:: pass_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.pass_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: satellite_pass
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.satellite_pass
    :type: IVehicleGraphics2DPass

    Get the pass property.

.. py:property:: visible_sides
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.visible_sides
    :type: VehicleGraphics2DVisibleSideType

    Gets or sets the visible sides option for the pass: ascending, descending, both or none.

.. py:property:: show_pass_labels
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.show_pass_labels
    :type: bool

    Opt whether to display pass numbers at the pass break locations in the 2D Graphics window.

.. py:property:: show_path_labels
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.show_path_labels
    :type: bool

    Opt whether to display path numbers within a repeating ground track sequence at the pass break locations in the 2D Graphics window.


Method detail
-------------


.. py:method:: set_pass_type(self, pass_type: VehicleGraphics2DPass) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.set_pass_type

    Pass display option: show all or those in a user-specified range.

    :Parameters:

    **pass_type** : :obj:`~VehicleGraphics2DPass`

    :Returns:

        :obj:`~None`

.. py:method:: is_pass_type_supported(self, pass_type: VehicleGraphics2DPass) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DPasses.is_pass_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **pass_type** : :obj:`~VehicleGraphics2DPass`

    :Returns:

        :obj:`~bool`









