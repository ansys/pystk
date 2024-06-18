IPlaceGraphics3D
================

.. py:class:: IPlaceGraphics3D

   object
   
   IAgPlaceVO Interface. For 3D properties of a Place object.

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

    from ansys.stk.core.stkobjects import IPlaceGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.model
    :type: "IAgPtTargetVOModel"

    Returns the 3D model properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.offsets
    :type: "IAgVOOffset"

    Returns the 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.range_contours
    :type: "IAgVORangeContours"

    Returns the 3D range contours properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.data_displays
    :type: "IAgVODataDisplayCollection"

    Returns the 3D data display properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.vector
    :type: "IAgVOVector"

    Returns the 3D vectorector properties.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.az_el_mask
    :type: "IAgVOAzElMask"

    Returns the 3D AzElMask properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.model_pointing
    :type: "IAgVOModelPointing"

    Returns 3D model pointing properties used to point parts of a place model toward a place, such as the Sun or Earth.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.aou_label_swap_distance
    :type: "IAgVOLabelSwapDistance"

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.vapor_trail
    :type: "IAgVOVaporTrail"

    Vapor trail attributes.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics3D.radar_cross_section
    :type: "IAgRadarCrossSectionVO"

    Gets the radar cross section graphics interface.


