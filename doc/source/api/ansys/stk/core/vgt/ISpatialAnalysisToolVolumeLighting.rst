ISpatialAnalysisToolVolumeLighting
==================================

.. py:class:: ISpatialAnalysisToolVolumeLighting

   object
   
   A lighting volume interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~eclipsing_bodies`
            * - :py:meth:`~use_object_eclipsing_bodies`
            * - :py:meth:`~lighting_conditions`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeLighting


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeLighting.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeLighting.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.

.. py:property:: lighting_conditions
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeLighting.lighting_conditions
    :type: CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE

    Sets/Returns the lighting conditions.


