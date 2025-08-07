ScriptingCalculationObject
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject

   Calc Object.

.. py:currentmodule:: ScriptingCalculationObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.copy_calculation_object_to_clipboard`
              - Copy the wrapped calc object to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.paste_calculation_object_from_clipboard`
              - Replace the wrapped calc object with the instance in the clipboard.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.calculation_object`
              - Get or set the calculation object type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.calculation_object_name`
              - Get or set the name of the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.component_name`
              - Get or set the name of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.unit`
              - Get or set the unit.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingCalculationObject


Property detail
---------------

.. py:property:: calculation_object
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.calculation_object
    :type: IComponentInfo

    Get or set the calculation object type.

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.calculation_object_name
    :type: str

    Get or set the name of the calculation object.

.. py:property:: component_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.component_name
    :type: str

    Get or set the name of the component.

.. py:property:: unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.unit
    :type: str

    Get or set the unit.


Method detail
-------------







.. py:method:: copy_calculation_object_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.copy_calculation_object_to_clipboard

    Copy the wrapped calc object to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_calculation_object_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject.paste_calculation_object_from_clipboard

    Replace the wrapped calc object with the instance in the clipboard.

    :Returns:

        :obj:`~None`



