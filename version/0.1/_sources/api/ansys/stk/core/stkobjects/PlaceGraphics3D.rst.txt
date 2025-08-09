PlaceGraphics3D
===============

.. py:class:: ansys.stk.core.stkobjects.PlaceGraphics3D

   3D Graphics properties of a Place.

.. py:currentmodule:: PlaceGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.model`
              - Return the 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.offsets`
              - Return the 3D offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.range_contours`
              - Return the 3D range contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.data_displays`
              - Return the 3D data display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.vector`
              - Return the 3D vectorector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.az_el_mask`
              - Return the 3D AzElMask properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.model_pointing`
              - Return 3D model pointing properties used to point parts of a place model toward a place, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.uncertainty_area_label_swap_distance`
              - Area of uncertainty label swap distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlaceGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.model
    :type: PointTargetGraphics3DModel

    Return the 3D model properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.offsets
    :type: Graphics3DOffset

    Return the 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Return the 3D range contours properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.data_displays
    :type: Graphics3DDataDisplayCollection

    Return the 3D data display properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.vector
    :type: Graphics3DVector

    Return the 3D vectorector properties.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.az_el_mask
    :type: Graphics3DAzElMask

    Return the 3D AzElMask properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Return 3D model pointing properties used to point parts of a place model toward a place, such as the Sun or Earth.

.. py:property:: uncertainty_area_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.uncertainty_area_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.


