TargetGraphics3D
================

.. py:class:: ansys.stk.core.stkobjects.TargetGraphics3D

   Class defining 3D Graphics for a Target object.

.. py:currentmodule:: TargetGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.az_el_mask`
              - Return the 3D AzElMask properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.data_displays`
              - Return the 3D data display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.model`
              - Return the 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.model_pointing`
              - Return 3D model pointing properties used to point parts of a target model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.offsets`
              - Return the 3D offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.range_contours`
              - Return the 3D range contours properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.uncertainty_area_label_swap_distance`
              - Area of uncertainty label swap distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.TargetGraphics3D.vector`
              - Return the 3D vectorector properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TargetGraphics3D


Property detail
---------------

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.az_el_mask
    :type: Graphics3DAzElMask

    Return the 3D AzElMask properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.data_displays
    :type: Graphics3DDataDisplayCollection

    Return the 3D data display properties.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.model
    :type: PointTargetGraphics3DModel

    Return the 3D model properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Return 3D model pointing properties used to point parts of a target model toward a target, such as the Sun or Earth.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.offsets
    :type: Graphics3DOffset

    Return the 3D offsets properties.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Return the 3D range contours properties.

.. py:property:: uncertainty_area_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.uncertainty_area_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.TargetGraphics3D.vector
    :type: Graphics3DVector

    Return the 3D vectorector properties.


