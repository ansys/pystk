IProfileScriptingTool
=====================

.. py:class:: IProfileScriptingTool

   IProfile
   
   Properties for a Scripting Tool profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~script_text`
              - Injects the script into the scripting tool.
            * - :py:meth:`~copy_to_clipboard`
              - Copy entire scripting tool to clipboard.
            * - :py:meth:`~paste_from_clipboard`
              - Replace entire scripting tool with scripting tool in clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable`
            * - :py:meth:`~segment_properties`
            * - :py:meth:`~calc_objects`
            * - :py:meth:`~parameters`
            * - :py:meth:`~language_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileScriptingTool


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.enable
    :type: bool

    If true, the scripting tool will be used.

.. py:property:: segment_properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.segment_properties
    :type: IAgVAScriptingSegmentCollection

    Returns the collection of the segment properties.

.. py:property:: calc_objects
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.calc_objects
    :type: IAgVAScriptingCalcObjectCollection

    Returns the collection of the calc objects.

.. py:property:: parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.parameters
    :type: IAgVAScriptingParameterCollection

    Returns the collection of parameters.

.. py:property:: language_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.language_type
    :type: LANGUAGE

    Gets or sets the scripting language being used.


Method detail
-------------








.. py:method:: script_text(self, script: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.script_text

    Injects the script into the scripting tool.

    :Parameters:

    **script** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.copy_to_clipboard

    Copy entire scripting tool to clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool.paste_from_clipboard

    Replace entire scripting tool with scripting tool in clipboard.

    :Returns:

        :obj:`~None`

