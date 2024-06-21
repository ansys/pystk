IVehicleGraphics2DPasses
========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses

   object
   
   Interface for setting satellite pass display graphics.

.. py:currentmodule:: IVehicleGraphics2DPasses

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.set_pass_type`
              - Pass display option: show all or those in a user-specified range.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_pass_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_method`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.visible_sides`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_pass_labels_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_path_labels_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DPasses


Property detail
---------------

.. py:property:: pass_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_type
    :type: VEHICLE_GRAPHICS_2D_PASS

    Pass display option: show all or those in a user-specified range.

.. py:property:: pass_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: pass_method
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.pass_method
    :type: IVehicleGraphics2DPass

    Get the pass property.

.. py:property:: visible_sides
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.visible_sides
    :type: VEHICLE_GRAPHICS_2D_VISIBLE_SIDES

    Gets or sets the visible sides option for the pass: ascending, descending, both or none.

.. py:property:: is_pass_labels_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_pass_labels_visible
    :type: bool

    Opt whether to display pass numbers at the pass break locations in the 2D Graphics window.

.. py:property:: is_path_labels_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_path_labels_visible
    :type: bool

    Opt whether to display path numbers within a repeating ground track sequence at the pass break locations in the 2D Graphics window.


Method detail
-------------


.. py:method:: set_pass_type(self, passType: VEHICLE_GRAPHICS_2D_PASS) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.set_pass_type

    Pass display option: show all or those in a user-specified range.

    :Parameters:

    **passType** : :obj:`~VEHICLE_GRAPHICS_2D_PASS`

    :Returns:

        :obj:`~None`

.. py:method:: is_pass_type_supported(self, passType: VEHICLE_GRAPHICS_2D_PASS) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DPasses.is_pass_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **passType** : :obj:`~VEHICLE_GRAPHICS_2D_PASS`

    :Returns:

        :obj:`~bool`









