SpatialAnalysisToolCalculationFile
==================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

.. py:currentmodule:: SpatialAnalysisToolCalculationFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile.reload`
              - Reload the volume calc file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile.filename`
              - The path of an external file that contains the volume calc data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolCalculationFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile.filename
    :type: str

    The path of an external file that contains the volume calc data.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile.reload

    Reload the volume calc file.

    :Returns:

        :obj:`~None`

