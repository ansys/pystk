ISpatialAnalysisToolVolumeCalcAltitude
======================================

.. py:class:: ISpatialAnalysisToolVolumeCalcAltitude

   object
   
   A volume calc altitude interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~shape_model`
            * - :py:meth:`~use_custom_reference`
            * - :py:meth:`~reference_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcAltitude


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcAltitude.central_body
    :type: str

    Get the central body for the volume calc. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume calc.

.. py:property:: shape_model
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcAltitude.shape_model
    :type: CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE

    The Volume Calc Altitude Reference Type.

.. py:property:: use_custom_reference
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcAltitude.use_custom_reference
    :type: bool

    Whether to use custom reference.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcAltitude.reference_point
    :type: IAgCrdnPoint

    A reference point. Can be any point from VGT.


