IVehicleGraphics2DTimeComponentsEventCollectionElement
======================================================

.. py:class:: IVehicleGraphics2DTimeComponentsEventCollectionElement

   IVehicleGraphics2DTimeComponentsElement
   
   Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_time_component`
              - Return an instance of a time component which provides the time intervals to control the appearance and visibility of the graphics path. The method may throw an exception if the component is invalid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_color_ramp`
            * - :py:meth:`~color_ramp_start_color`
            * - :py:meth:`~color_ramp_end_color`
            * - :py:meth:`~umbra`
            * - :py:meth:`~penumbra`
            * - :py:meth:`~sunlight`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeComponentsEventCollectionElement


Property detail
---------------

.. py:property:: use_color_ramp
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.use_color_ramp
    :type: bool

    Whether the color ramp is used. Setting this property has no effect if the color ramp is not supported.

.. py:property:: color_ramp_start_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.color_ramp_start_color
    :type: agcolor.Color

    The start color of the color ramp. Setting this property has no effect if the color ramp is not supported.

.. py:property:: color_ramp_end_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.color_ramp_end_color
    :type: agcolor.Color

    The end color of the color ramp. Setting this property has no effect if the color ramp is not supported.

.. py:property:: umbra
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.umbra
    :type: "IAgVeGfxAttributesBasic"

    Configure the appearance of the orbit track, the marker, etc. when the vehicle isn't in sunlight at all.

.. py:property:: penumbra
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.penumbra
    :type: "IAgVeGfxAttributesBasic"

    Configure the appearance of the orbit track, the marker, etc. when the vehicle is only partially in sunlight.

.. py:property:: sunlight
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventCollectionElement.sunlight
    :type: "IAgVeGfxAttributesBasic"

    Configure the appearance of the orbit track, the marker, etc. when the vehicle is in complete sunlight.


Method detail
-------------










.. py:method:: get_time_component(self) -> "IAnalysisWorkbenchComponent"

    Return an instance of a time component which provides the time intervals to control the appearance and visibility of the graphics path. The method may throw an exception if the component is invalid.

    :Returns:

        :obj:`~"IAnalysisWorkbenchComponent"`

