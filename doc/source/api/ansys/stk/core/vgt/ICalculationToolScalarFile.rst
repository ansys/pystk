ICalculationToolScalarFile
==========================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarFile

   object
   
   Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

.. py:currentmodule:: ICalculationToolScalarFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.reload`
              - Reload the file specified with Filename property.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.get_file_span`
              - Compute the interval time span of the file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.filename`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.file_interpolation_type`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.file_interpolation_order`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFile.use_native_file_interpolation_settings`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.filename
    :type: str

    The path to an ASCII file with .csc extension.

.. py:property:: file_interpolation_type
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.file_interpolation_type
    :type: CRDN_FILE_INTERPOLATOR_TYPE

    The interpolation method used with the data.

.. py:property:: file_interpolation_order
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.file_interpolation_order
    :type: int

    The interpolation order used with the interpolation method to interrogate the data.

.. py:property:: use_native_file_interpolation_settings
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.use_native_file_interpolation_settings
    :type: bool

    Flag indicating whether the interpolation method and order settings specified within the file, if any, will be honored.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.reload

    Reload the file specified with Filename property.

    :Returns:

        :obj:`~None`

.. py:method:: get_file_span(self) -> ITimeToolEventIntervalResult
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFile.get_file_span

    Compute the interval time span of the file.

    :Returns:

        :obj:`~ITimeToolEventIntervalResult`







