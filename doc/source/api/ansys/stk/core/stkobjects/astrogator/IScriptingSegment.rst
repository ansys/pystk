IScriptingSegment
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IScriptingSegment

   object
   
   Object properties for scripting options.

.. py:currentmodule:: IScriptingSegment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.component_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.attribute`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.available_attribute_values`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.read_only_property`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.object_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment.available_object_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingSegment


Property detail
---------------

.. py:property:: component_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.component_name
    :type: str

    Gets or sets the name of the component.

.. py:property:: attribute
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.attribute
    :type: str

    Gets or sets the name of the attribute.

.. py:property:: unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.unit
    :type: str

    Gets or sets the unit.

.. py:property:: available_attribute_values
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.available_attribute_values
    :type: list

    Returns a list of available attribute values.

.. py:property:: read_only_property
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.read_only_property
    :type: bool

    True if it is a read-only property.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.object_name
    :type: str

    Gets or sets the profile/segment that contains the attribute.

.. py:property:: available_object_names
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegment.available_object_names
    :type: list

    Returns a list of available profile/segment names.


