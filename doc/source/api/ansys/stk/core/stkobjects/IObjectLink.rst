IObjectLink
===========

.. py:class:: IObjectLink

   object
   
   IAgObjectLink provides methods and properties of elements stored in IAgObjectLinkCollection collection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~path`
            * - :py:meth:`~type`
            * - :py:meth:`~linked_object`


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
    :type: IAgStkObject

    Returns the STK object associated with the instance.


