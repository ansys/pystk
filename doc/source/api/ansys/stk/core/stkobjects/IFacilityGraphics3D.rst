IFacilityGraphics3D
===================

.. py:class:: IFacilityGraphics3D

   object
   
   AgFaVO Interface. For 3D properties of a Facility object interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model`
            * - :py:meth:`~offsets`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~data_displays`
            * - :py:meth:`~vector`
            * - :py:meth:`~az_el_mask`
            * - :py:meth:`~model_pointing`
            * - :py:meth:`~aou_label_swap_distance`
            * - :py:meth:`~vapor_trail`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFacilityGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.model
    :type: IAgPtTargetVOModel

    Returns Model properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.offsets
    :type: IAgVOOffset

    Returns Offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.range_contours
    :type: IAgVORangeContours

    Returns Range Contours properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.data_displays
    :type: IAgVODataDisplayCollection

    Returns DataDisplays collection.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.vector
    :type: IAgVOVector

    Returns a vector.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.az_el_mask
    :type: IAgVOAzElMask

    Returns the AzElMask property.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.model_pointing
    :type: IAgVOModelPointing

    Returns ModelPointing properties used to point parts of a facility model toward a target, such as the Sun or Earth.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.aou_label_swap_distance
    :type: IAgVOLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.vapor_trail
    :type: IAgVOVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics3D.radar_cross_section
    :type: IAgRadarCrossSectionVO

    Gets the radar cross section graphics interface.


