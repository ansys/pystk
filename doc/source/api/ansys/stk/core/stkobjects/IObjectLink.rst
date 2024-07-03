IObjectLink
===========

.. py:class:: ansys.stk.core.stkobjects.IObjectLink

   object
   
   IAgObjectLink provides methods and properties of elements stored in IAgObjectLinkCollection collection.

.. py:currentmodule:: IObjectLink

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLink.name`
              - Returns STK object name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLink.path`
              - Returns STK object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLink.type`
              - Returns STK object type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLink.linked_object`
              - Returns the STK object associated with the instance.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IObjectLink


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IObjectLink.name
    :type: str

    Returns STK object name.

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.IObjectLink.path
    :type: str

    Returns STK object path.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IObjectLink.type
    :type: STK_OBJECT_TYPE

    Returns STK object type.

.. py:property:: linked_object
    :canonical: ansys.stk.core.stkobjects.IObjectLink.linked_object
    :type: IStkObject

    Returns the STK object associated with the instance.


