IVehicleGraphics2DAttributesAccess
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess

   IVehicleGraphics2DAttributes
   
   Vehicle 2D Graphics display based on access intervals.

.. py:currentmodule:: IVehicleGraphics2DAttributesAccess

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.access_objects`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.during_access`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.no_access`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesAccess


Property detail
---------------

.. py:property:: access_objects
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.access_objects
    :type: IObjectLinkCollection

    Returns the collection of objects used for the access.

.. py:property:: during_access
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.during_access
    :type: IVehicleGraphics2DAttributesBasic

    Returns the collection of gfx attributes used during the access.

.. py:property:: no_access
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesAccess.no_access
    :type: IVehicleGraphics2DAttributesBasic

    Returns the collection of gfx attributes used when there is no access.


