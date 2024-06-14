ISatelliteGraphics
==================

.. py:class:: ISatelliteGraphics

   object
   
   Satellite 2D Graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attributes_type`
              - Set the attributes type.
            * - :py:meth:`~is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~attributes_type`
            * - :py:meth:`~attributes_supported_types`
            * - :py:meth:`~attributes`
            * - :py:meth:`~time_events`
            * - :py:meth:`~passes`
            * - :py:meth:`~pass_data`
            * - :py:meth:`~resolution`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~saa`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~lighting`
            * - :py:meth:`~swath`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~ground_track_central_body_display`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~label_name`
            * - :py:meth:`~is_object_graphics_visible`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatelliteGraphics


Property detail
---------------

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.attributes_type
    :type: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"

    Type of 2D Graphics attributes: basic, access intervals or custom intervals.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.attributes
    :type: "IAgVeGfxAttributes"

    Get the satellite's 2D Graphics Attributes.

.. py:property:: time_events
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.time_events
    :type: "IAgVeGfxTimeEventsCollection"

    Get the satellite's TimeEvents properties.

.. py:property:: passes
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.passes
    :type: "IAgVeGfxPasses"

    Get the pass display settings of the satellite's Pass properties.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.pass_data
    :type: "IAgVeGfxOrbitPassData"

    Get the leading/trailing ground track and orbit settings of the satellite's Pass properties.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.resolution
    :type: "IAgVeGfxPassResolution"

    Get the path resolution settings of the satellite's Pass properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.elev_contours
    :type: "IAgVeGfxElevContours"

    Get the satellite's Elevation Contours properties.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.saa
    :type: "IAgVeGfxSAA"

    Get the satellite's South Atlantic Anomaly Contour properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.range_contours
    :type: "IAgGfxRangeContours"

    Get the satellite's Range Contours properties.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.lighting
    :type: "IAgVeGfxLighting"

    Get the satellite's Lighting properties.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.swath
    :type: "IAgVeGfxSwath"

    Get the satellite's Swath properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.ground_ellipses
    :type: "IAgVeGfxGroundEllipsesCollection"

    Get the satellite's Ground Ellipses properties.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.label_notes
    :type: "IAgLabelNoteCollection"

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: ground_track_central_body_display
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.ground_track_central_body_display
    :type: "IAgVeCentralBodies"

    Gets the ground track display central bodies.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the satellite (as shown in the Object Browser) as its label.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.label_name
    :type: str

    The user-specified name to use as a label for the satellite.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the satellite are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ISatelliteGraphics.radar_cross_section
    :type: "IAgRadarCrossSectionGraphics"

    Gets the radar cross section graphics interface.


Method detail
-------------


.. py:method:: set_attributes_type(self, attributes:"VEHICLE_GRAPHICS_2D_ATTRIBUTES") -> None

    Set the attributes type.

    :Parameters:

    **attributes** : :obj:`~"VEHICLE_GRAPHICS_2D_ATTRIBUTES"`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes:"VEHICLE_GRAPHICS_2D_ATTRIBUTES") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~"VEHICLE_GRAPHICS_2D_ATTRIBUTES"`

    :Returns:

        :obj:`~bool`






















