SpatialAnalysisToolVolumeCalcFile
=================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalc`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

.. py:currentmodule:: SpatialAnalysisToolVolumeCalcFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile.reload`
              - Reload the volume calc file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile.filename`
              - The path of an external file that contains the volume calc data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeCalcFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile.filename
    :type: str

    The path of an external file that contains the volume calc data.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile.reload

    Reload the volume calc file.

    :Returns:

        :obj:`~None`

