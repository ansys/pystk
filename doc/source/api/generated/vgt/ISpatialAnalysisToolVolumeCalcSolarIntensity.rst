ISpatialAnalysisToolVolumeCalcSolarIntensity
============================================

.. py:class:: ISpatialAnalysisToolVolumeCalcSolarIntensity

   object
   
   A volume calc solar intensityn interface.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcSolarIntensity


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcSolarIntensity.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcSolarIntensity.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


