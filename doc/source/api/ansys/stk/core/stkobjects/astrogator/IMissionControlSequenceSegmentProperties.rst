IMissionControlSequenceSegmentProperties
========================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties

   object
   
   The segment properties.

.. py:currentmodule:: IMissionControlSequenceSegmentProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.apply_final_state_to_b_planes`
              - Apply the last calculated final state of the segment to all selected B-Planes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.display_coordinate_system`
              - Gets or sets the coordinate system that will be used in the segment summary report.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.color`
              - Gets or sets the display color of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.update_animation_time_after_run`
              - If true, Astrogator will set the animation time to the final epoch of the segment when the segment finishes running.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.b_planes`
              - Get the B-Plane or B-Planes to which the epoch, position, and velocity of the segment's final state will be applied, according to the B-Plane's definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.last_run_code`
              - Get the last run code returned by the segment.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceSegmentProperties


Property detail
---------------

.. py:property:: display_coordinate_system
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.display_coordinate_system
    :type: str

    Gets or sets the coordinate system that will be used in the segment summary report.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.color
    :type: agcolor.Color

    Gets or sets the display color of the segment.

.. py:property:: update_animation_time_after_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.update_animation_time_after_run
    :type: bool

    If true, Astrogator will set the animation time to the final epoch of the segment when the segment finishes running.

.. py:property:: b_planes
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.b_planes
    :type: IBPlaneCollection

    Get the B-Plane or B-Planes to which the epoch, position, and velocity of the segment's final state will be applied, according to the B-Plane's definition.

.. py:property:: last_run_code
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.last_run_code
    :type: RUN_CODE

    Get the last run code returned by the segment.


Method detail
-------------







.. py:method:: apply_final_state_to_b_planes(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties.apply_final_state_to_b_planes

    Apply the last calculated final state of the segment to all selected B-Planes.

    :Returns:

        :obj:`~None`



