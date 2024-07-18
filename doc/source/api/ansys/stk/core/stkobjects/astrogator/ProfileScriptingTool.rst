ProfileScriptingTool
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Scripting Tool profile.

.. py:currentmodule:: ProfileScriptingTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.script_text`
              - Injects the script into the scripting tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.copy_to_clipboard`
              - Copy entire scripting tool to clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.paste_from_clipboard`
              - Replace entire scripting tool with scripting tool in clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.enable`
              - If true, the scripting tool will be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.segment_properties`
              - Returns the collection of the segment properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.calc_objects`
              - Returns the collection of the calc objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.parameters`
              - Returns the collection of parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.language_type`
              - Gets or sets the scripting language being used.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileScriptingTool


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.enable
    :type: bool

    If true, the scripting tool will be used.

.. py:property:: segment_properties
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.segment_properties
    :type: IScriptingSegmentCollection

    Returns the collection of the segment properties.

.. py:property:: calc_objects
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.calc_objects
    :type: IScriptingCalcObjectCollection

    Returns the collection of the calc objects.

.. py:property:: parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.parameters
    :type: IScriptingParameterCollection

    Returns the collection of parameters.

.. py:property:: language_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.language_type
    :type: LANGUAGE

    Gets or sets the scripting language being used.


Method detail
-------------








.. py:method:: script_text(self, script: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.script_text

    Injects the script into the scripting tool.

    :Parameters:

    **script** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.copy_to_clipboard

    Copy entire scripting tool to clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool.paste_from_clipboard

    Replace entire scripting tool with scripting tool in clipboard.

    :Returns:

        :obj:`~None`

