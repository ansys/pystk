ISpatialAnalysisToolVolumeGridResult
====================================

.. py:class:: ISpatialAnalysisToolVolumeGridResult

   object
   
   An interface that generates Volume Grid results.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~epoch`
            * - :py:meth:`~size_i`
            * - :py:meth:`~size_j`
            * - :py:meth:`~size_k`
            * - :py:meth:`~volume_metric_data_vector`
            * - :py:meth:`~volume_metric_position_vector`
            * - :py:meth:`~volume_metric_native_position_vector`
            * - :py:meth:`~volume_metric_gradient_vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridResult


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.epoch
    :type: typing.Any

    Epoch of returned volumetric data.

.. py:property:: size_i
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.size_i
    :type: int

    Number of grid point coordinates representing first dimension of volume grid.

.. py:property:: size_j
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.size_j
    :type: int

    Number of grid point coordinates representing second dimension of volume grid.

.. py:property:: size_k
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.size_k
    :type: int

    Number of grid point coordinates representing third dimension of volume grid.

.. py:property:: volume_metric_data_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.volume_metric_data_vector
    :type: list

    Vector of scalar values representing volumetric data.

.. py:property:: volume_metric_position_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.volume_metric_position_vector
    :type: list

    Vector of Cartesian coordinates of all volume grid points.

.. py:property:: volume_metric_native_position_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.volume_metric_native_position_vector
    :type: list

    Vector of native coordinates of all volume grid points.

.. py:property:: volume_metric_gradient_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridResult.volume_metric_gradient_vector
    :type: list

    Vector of Cartesian coordinates representing gradient vectors at all volume grid points.


