IScriptingCalcObject
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject

   object
   
   Calc Object properties for scripting options.

.. py:currentmodule:: IScriptingCalcObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.copy_calc_object_to_clipboard`
              - Copy the wrapped calc object to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.paste_calc_object_from_clipboard`
              - Replace the wrapped calc object with the instance in the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.component_name`
              - Gets or sets the name of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.calc_object_name`
              - Gets or sets the name of the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.calc_object`
              - Gets or sets the calculation object type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.unit`
              - Gets or sets the unit.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingCalcObject


Property detail
---------------

.. py:property:: component_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.component_name
    :type: str

    Gets or sets the name of the component.

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.calc_object_name
    :type: str

    Gets or sets the name of the calculation object.

.. py:property:: calc_object
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.calc_object
    :type: IComponentInfo

    Gets or sets the calculation object type.

.. py:property:: unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.unit
    :type: str

    Gets or sets the unit.


Method detail
-------------









.. py:method:: copy_calc_object_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.copy_calc_object_to_clipboard

    Copy the wrapped calc object to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_calc_object_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject.paste_calc_object_from_clipboard

    Replace the wrapped calc object with the instance in the clipboard.

    :Returns:

        :obj:`~None`

