CalculationToolScalarFile
=========================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarFile

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

.. py:currentmodule:: CalculationToolScalarFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.reload`
              - Reload the file specified with Filename property.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.get_file_span`
              - Compute the interval time span of the file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.filename`
              - The path to an ASCII file with .csc extension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.file_interpolation_type`
              - The interpolation method used with the data.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.file_interpolation_order`
              - The interpolation order used with the interpolation method to interrogate the data.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile.use_native_file_interpolation_settings`
              - Flag indicating whether the interpolation method and order settings specified within the file, if any, will be honored.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.filename
    :type: str

    The path to an ASCII file with .csc extension.

.. py:property:: file_interpolation_type
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.file_interpolation_type
    :type: FileInterpolatorType

    The interpolation method used with the data.

.. py:property:: file_interpolation_order
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.file_interpolation_order
    :type: int

    The interpolation order used with the interpolation method to interrogate the data.

.. py:property:: use_native_file_interpolation_settings
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.use_native_file_interpolation_settings
    :type: bool

    Flag indicating whether the interpolation method and order settings specified within the file, if any, will be honored.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.reload

    Reload the file specified with Filename property.

    :Returns:

        :obj:`~None`

.. py:method:: get_file_span(self) -> TimeToolTimeIntervalResult
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFile.get_file_span

    Compute the interval time span of the file.

    :Returns:

        :obj:`~TimeToolTimeIntervalResult`







