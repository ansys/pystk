SpatialAnalysisToolVolumeGridConstrained
========================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid constrained interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.reference_grid`
              - Get the reference system in which spherical parameters are computed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.constraint`
              - Get the volume constraint on the grid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridConstrained


Property detail
---------------

.. py:property:: reference_grid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.reference_grid
    :type: ISpatialAnalysisToolVolumeGrid

    Get the reference system in which spherical parameters are computed.

.. py:property:: constraint
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on the grid.


