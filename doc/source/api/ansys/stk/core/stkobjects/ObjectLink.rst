ObjectLink
==========

.. py:class:: ansys.stk.core.stkobjects.ObjectLink

   Class defining name of an STK object.

.. py:currentmodule:: ObjectLink

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectLink.name`
              - Returns STK object name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectLink.path`
              - Returns STK object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectLink.type`
              - Returns STK object type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectLink.linked_object`
              - Returns the STK object associated with the instance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ObjectLink


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.ObjectLink.name
    :type: str

    Returns STK object name.

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.ObjectLink.path
    :type: str

    Returns STK object path.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.ObjectLink.type
    :type: STK_OBJECT_TYPE

    Returns STK object type.

.. py:property:: linked_object
    :canonical: ansys.stk.core.stkobjects.ObjectLink.linked_object
    :type: IStkObject

    Returns the STK object associated with the instance.


