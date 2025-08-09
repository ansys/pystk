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
              - Return Model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.offsets`
              - Return Offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.range_contours`
              - Return Range Contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.data_displays`
              - Return DataDisplays collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.vector`
              - Return a vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.az_el_mask`
              - Return the AzElMask property.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.model_pointing`
              - Return ModelPointing properties used to point parts of a facility model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.uncertainty_area_label_swap_distance`
              - Area of uncertainty label swap distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FacilityGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.model
    :type: PointTargetGraphics3DModel

    Return Model properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.offsets
    :type: Graphics3DOffset

    Return Offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Return Range Contours properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.data_displays
    :type: Graphics3DDataDisplayCollection

    Return DataDisplays collection.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.vector
    :type: Graphics3DVector

    Return a vector.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.az_el_mask
    :type: Graphics3DAzElMask

    Return the AzElMask property.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Return ModelPointing properties used to point parts of a facility model toward a target, such as the Sun or Earth.

.. py:property:: uncertainty_area_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.uncertainty_area_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.


