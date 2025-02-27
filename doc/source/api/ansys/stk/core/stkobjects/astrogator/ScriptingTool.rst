ScriptingTool
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingTool

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Tool.

.. py:currentmodule:: ScriptingTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.script_text`
              - Injects the script into the scripting tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.copy_to_clipboard`
              - Copy entire scripting tool to clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.paste_from_clipboard`
              - Replace entire scripting tool with scripting tool in clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.enable`
              - If true, the scripting tool is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.segment_properties`
              - Return the collection of the segment properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.calculation_objects`
              - Return the collection of the calculation objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.parameters`
              - Return the collection of parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.language_type`
              - Get or set the scripting language being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool.pre_iterate`
              - If true, the sequence will run once before executing the script.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingTool


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.enable
    :type: bool

    If true, the scripting tool is enabled.

.. py:property:: segment_properties
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.segment_properties
    :type: ScriptingSegmentCollection

    Return the collection of the segment properties.

.. py:property:: calculation_objects
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.calculation_objects
    :type: ScriptingCalculationObjectCollection

    Return the collection of the calculation objects.

.. py:property:: parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.parameters
    :type: ScriptingParameterCollection

    Return the collection of parameters.

.. py:property:: language_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.language_type
    :type: Language

    Get or set the scripting language being used.

.. py:property:: pre_iterate
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.pre_iterate
    :type: bool

    If true, the sequence will run once before executing the script.


Method detail
-------------








.. py:method:: script_text(self, script: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.script_text

    Injects the script into the scripting tool.

    :Parameters:

    **script** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.copy_to_clipboard

    Copy entire scripting tool to clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingTool.paste_from_clipboard

    Replace entire scripting tool with scripting tool in clipboard.

    :Returns:

        :obj:`~None`



