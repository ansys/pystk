CalculationToolScalarCustomInlineScript
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

.. py:currentmodule:: CalculationToolScalarCustomInlineScript

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.get_all_arguments`
              - Return the list of arguments.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.set_all_arguments`
              - Set the list of arguments.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.script_type`
              - Script type allowed {JScript | Matlab | VBScript}.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.value_function`
              - The Value function to be evaluated.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.derivative_function`
              - The Derivative function to be evaluated.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.dimension`
              - Dimension name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarCustomInlineScript


Property detail
---------------

.. py:property:: script_type
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.script_type
    :type: str

    Script type allowed {JScript | Matlab | VBScript}.

.. py:property:: value_function
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.value_function
    :type: str

    The Value function to be evaluated.

.. py:property:: derivative_function
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.derivative_function
    :type: str

    The Derivative function to be evaluated.

.. py:property:: dimension
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.dimension
    :type: str

    Dimension name.


Method detail
-------------









.. py:method:: get_all_arguments(self) -> list
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.get_all_arguments

    Return the list of arguments.

    :Returns:

        :obj:`~list`

.. py:method:: set_all_arguments(self, calc_list: list) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript.set_all_arguments

    Set the list of arguments.

    :Parameters:

        **calc_list** : :obj:`~list`


    :Returns:

        :obj:`~None`

