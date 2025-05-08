SpatialAnalysisToolVolumeGridResult
===================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult

   An interface that generates Volume Grid results.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.epoch`
              - Epoch of returned volumetric data.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_i`
              - Number of grid point coordinates representing first dimension of volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_j`
              - Number of grid point coordinates representing second dimension of volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_k`
              - Number of grid point coordinates representing third dimension of volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.data_vector`
              - Vector of scalar values representing volumetric data.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.position_vector`
              - Vector of Cartesian coordinates of all volume grid points.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.native_position_vector`
              - Vector of native coordinates of all volume grid points.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.gradient_vector`
              - Vector of Cartesian coordinates representing gradient vectors at all volume grid points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridResult


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.epoch
    :type: typing.Any

    Epoch of returned volumetric data.

.. py:property:: size_i
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_i
    :type: int

    Number of grid point coordinates representing first dimension of volume grid.

.. py:property:: size_j
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_j
    :type: int

    Number of grid point coordinates representing second dimension of volume grid.

.. py:property:: size_k
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.size_k
    :type: int

    Number of grid point coordinates representing third dimension of volume grid.

.. py:property:: data_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.data_vector
    :type: list

    Vector of scalar values representing volumetric data.

.. py:property:: position_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.position_vector
    :type: list

    Vector of Cartesian coordinates of all volume grid points.

.. py:property:: native_position_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.native_position_vector
    :type: list

    Vector of native coordinates of all volume grid points.

.. py:property:: gradient_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult.gradient_vector
    :type: list

    Vector of Cartesian coordinates representing gradient vectors at all volume grid points.


