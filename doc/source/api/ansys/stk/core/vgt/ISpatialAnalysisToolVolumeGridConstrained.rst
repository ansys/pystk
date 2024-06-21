ISpatialAnalysisToolVolumeGridConstrained
=========================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained

   object
   
   A volume grid constrained interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeGridConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.reference_grid`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.constraint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridConstrained


Property detail
---------------

.. py:property:: reference_grid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.reference_grid
    :type: ISpatialAnalysisToolVolumeGrid

    Get the reference system in which spherical parameters are computed.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on the grid.


