SpatialAnalysisToolVolumeFromGrid
=================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An over time volume interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeFromGrid

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid.edge_type`
              - Sets/Returns the edge type.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid.volume_grid`
              - Sets/Returns the volume grid for bounding.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeFromGrid


Property detail
---------------

.. py:property:: edge_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid.edge_type
    :type: CRDN_VOLUME_FROM_GRID_EDGE_TYPE

    Sets/Returns the edge type.

.. py:property:: volume_grid
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid.volume_grid
    :type: ISpatialAnalysisToolVolumeGrid

    Sets/Returns the volume grid for bounding.


