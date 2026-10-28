StateCalcPythonScript
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Python script Calc objects.

.. py:currentmodule:: StateCalcPythonScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.calculation_object_arguments`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.calculation_object_arguments_link_embed`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.custom_script`
              - Get or set the user-supplied script to be evaluated as Python code.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.return_variable`
              - Get or set the name of the Python variable containing the calculated value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.unit_dimension`
              - Get or set the unit dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcPythonScript


Property detail
---------------

.. py:property:: calculation_object_arguments
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.calculation_object_arguments
    :type: CalculationObjectCollection

    Get the arguments to be applied to the function.

.. py:property:: calculation_object_arguments_link_embed
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.calculation_object_arguments_link_embed
    :type: CalculationObjectLinkEmbedControlCollection

    Get the arguments to be applied to the function.

.. py:property:: custom_script
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.custom_script
    :type: str

    Get or set the user-supplied script to be evaluated as Python code.

.. py:property:: return_variable
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.return_variable
    :type: str

    Get or set the name of the Python variable containing the calculated value.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcPythonScript.unit_dimension
    :type: str

    Get or set the unit dimension.


