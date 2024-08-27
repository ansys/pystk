FacilityGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.FacilityGraphics3D

   3D Graphics properties of a Facility.

.. py:currentmodule:: FacilityGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.model`
              - Returns Model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.offsets`
              - Returns Offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.range_contours`
              - Returns Range Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.data_displays`
              - Returns DataDisplays collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.vector`
              - Returns a vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.az_el_mask`
              - Returns the AzElMask property.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.model_pointing`
              - Returns ModelPointing properties used to point parts of a facility model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.aou_label_swap_distance`
              - Area of uncertainty label swap distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.radar_cross_section`
              - Gets the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FacilityGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.model
    :type: PointTargetGraphics3DModel

    Returns Model properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.offsets
    :type: Graphics3DOffset

    Returns Offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Returns Range Contours properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.data_displays
    :type: Graphics3DDataDisplayCollection

    Returns DataDisplays collection.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.vector
    :type: Graphics3DVector

    Returns a vector.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.az_el_mask
    :type: Graphics3DAzElMask

    Returns the AzElMask property.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Returns ModelPointing properties used to point parts of a facility model toward a target, such as the Sun or Earth.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.aou_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Gets the radar cross section graphics interface.


