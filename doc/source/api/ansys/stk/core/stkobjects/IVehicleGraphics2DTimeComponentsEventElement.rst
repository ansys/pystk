IVehicleGraphics2DTimeComponentsEventElement
============================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventElement

   IVehicleGraphics2DTimeComponentsElement
   
   Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

.. py:currentmodule:: IVehicleGraphics2DTimeComponentsEventElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventElement.get_time_component`
              - Return an instance of a time component which provides the time intervals to control the appearance and visibility of the graphics path. The method may throw an exception if the component is invalid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventElement.attributes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeComponentsEventElement


Property detail
---------------

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventElement.attributes
    :type: IVehicleGraphics2DAttributesBasic

    Returns the 2D attributes used to configure the appearance of ground tracks, orbits, etc. in 2D and 3D views.


Method detail
-------------


.. py:method:: get_time_component(self) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsEventElement.get_time_component

    Return an instance of a time component which provides the time intervals to control the appearance and visibility of the graphics path. The method may throw an exception if the component is invalid.

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

