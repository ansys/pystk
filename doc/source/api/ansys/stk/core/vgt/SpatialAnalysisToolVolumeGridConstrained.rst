SpatialAnalysisToolVolumeGridConstrained
========================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid constrained interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained.reference_grid`
              - Get the reference system in which spherical parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained.constraint`
              - Get the volume constraint on the grid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridConstrained


Property detail
---------------

.. py:property:: reference_grid
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained.reference_grid
    :type: ISpatialAnalysisToolVolumeGrid

    Get the reference system in which spherical parameters are computed.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on the grid.


