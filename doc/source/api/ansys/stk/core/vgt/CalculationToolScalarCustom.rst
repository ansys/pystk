CalculationToolScalarCustom
===========================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarCustom

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

.. py:currentmodule:: CalculationToolScalarCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarCustom.reload`
              - Reload the file specified with Filename property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarCustom.filename`
              - A path to MATLAB (.m or .dll), Perl or VBScript file.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarCustom.invalidate_on_execution_error`
              - Specify InvalidOnExecError flag for a custom scalar.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarCustom


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.CalculationToolScalarCustom.filename
    :type: str

    A path to MATLAB (.m or .dll), Perl or VBScript file.

.. py:property:: invalidate_on_execution_error
    :canonical: ansys.stk.core.vgt.CalculationToolScalarCustom.invalidate_on_execution_error
    :type: bool

    Specify InvalidOnExecError flag for a custom scalar.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolScalarCustom.reload

    Reload the file specified with Filename property.

    :Returns:

        :obj:`~None`



