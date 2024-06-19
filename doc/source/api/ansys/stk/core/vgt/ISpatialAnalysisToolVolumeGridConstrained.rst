ISpatialAnalysisToolVolumeGridConstrained
=========================================

.. py:class:: ISpatialAnalysisToolVolumeGridConstrained

   object
   
   A volume grid constrained interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_grid`
            * - :py:meth:`~constraint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridConstrained


Property detail
---------------

.. py:property:: reference_grid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.reference_grid
    :type: IAgCrdnVolumeGrid

    Get the reference system in which spherical parameters are computed.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridConstrained.constraint
    :type: IAgCrdnVolume

    Get the volume constraint on the grid.


