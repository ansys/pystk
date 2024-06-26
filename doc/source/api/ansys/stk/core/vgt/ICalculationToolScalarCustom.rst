ICalculationToolScalarCustom
============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarCustom

   object
   
   A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

.. py:currentmodule:: ICalculationToolScalarCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarCustom.reload`
              - Reload the file specified with Filename property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarCustom.filename`
              - A path to MATLAB (.m or .dll), Perl or VBScript file.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarCustom.invalidate_on_exec_error`
              - Specifies InvalidOnExecError flag for a custom scalar.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarCustom


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarCustom.filename
    :type: str

    A path to MATLAB (.m or .dll), Perl or VBScript file.

.. py:property:: invalidate_on_exec_error
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarCustom.invalidate_on_exec_error
    :type: bool

    Specifies InvalidOnExecError flag for a custom scalar.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarCustom.reload

    Reload the file specified with Filename property.

    :Returns:

        :obj:`~None`



