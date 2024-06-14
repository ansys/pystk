ISpatialAnalysisToolVolumeCalcRange
===================================

.. py:class:: ISpatialAnalysisToolVolumeCalcRange

   object
   
   A volume calc distance to location interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~distance`
            * - :py:meth:`~reference_point`
            * - :py:meth:`~reference_plane`
            * - :py:meth:`~along_vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcRange


Property detail
---------------

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.distance
    :type: "CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE"

    The Volume Calc range distance types.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_point
    :type: "IAgCrdnPoint"

    The Volume Calc Range reference point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_plane
    :type: "IAgCrdnPlane"

    The Volume Calc Range reference plane.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.along_vector
    :type: "IAgCrdnVector"

    The Volume Calc Range Along Vector.


