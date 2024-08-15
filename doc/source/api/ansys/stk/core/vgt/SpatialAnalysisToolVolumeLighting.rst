SpatialAnalysisToolVolumeLighting
=================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A lighting volume interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeLighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.lighting_conditions`
              - Sets/Returns the lighting conditions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeLighting


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.

.. py:property:: lighting_conditions
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting.lighting_conditions
    :type: CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE

    Sets/Returns the lighting conditions.


