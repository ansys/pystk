ISpatialAnalysisToolVolumeCalcFile
==================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFile

   object
   
   Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

.. py:currentmodule:: ISpatialAnalysisToolVolumeCalcFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFile.reload`
              - Reload the volume calc file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFile.filename`
              - The path of an external file that contains the volume calc data.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFile.filename
    :type: str

    The path of an external file that contains the volume calc data.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFile.reload

    Reload the volume calc file.

    :Returns:

        :obj:`~None`

