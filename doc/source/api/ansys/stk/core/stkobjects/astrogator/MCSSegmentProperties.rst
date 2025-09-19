MCSSegmentProperties
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Segment Properties.

.. py:currentmodule:: MCSSegmentProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.apply_final_state_to_b_planes`
              - Apply the last calculated final state of the segment to all selected B-Planes.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.b_planes`
              - Get the B-Plane or B-Planes to which the epoch, position, and velocity of the segment's final state will be applied, according to the B-Plane's definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.color`
              - Get or set the display color of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.display_coordinate_system`
              - Get or set the coordinate system that will be used in the segment summary report.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.last_run_code`
              - Get the last run code returned by the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.update_animation_time_after_run`
              - If true, Astrogator will set the animation time to the final epoch of the segment when the segment finishes running.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSSegmentProperties


Property detail
---------------

.. py:property:: b_planes
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.b_planes
    :type: BPlaneCollection

    Get the B-Plane or B-Planes to which the epoch, position, and velocity of the segment's final state will be applied, according to the B-Plane's definition.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.color
    :type: Color

    Get or set the display color of the segment.

.. py:property:: display_coordinate_system
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.display_coordinate_system
    :type: str

    Get or set the coordinate system that will be used in the segment summary report.

.. py:property:: last_run_code
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.last_run_code
    :type: RunCode

    Get the last run code returned by the segment.

.. py:property:: update_animation_time_after_run
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.update_animation_time_after_run
    :type: bool

    If true, Astrogator will set the animation time to the final epoch of the segment when the segment finishes running.


Method detail
-------------

.. py:method:: apply_final_state_to_b_planes(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties.apply_final_state_to_b_planes

    Apply the last calculated final state of the segment to all selected B-Planes.

    :Returns:

        :obj:`~None`









