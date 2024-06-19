ILinkToObject
=============

.. py:class:: ILinkToObject

   object
   
   IAgLinkToObject represents a link to STK object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bind_to`
              - Binds to existing object instance using the specified object path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~linked_object`
            * - :py:meth:`~available_objects`
            * - :py:meth:`~is_intrinsic`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILinkToObject


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.ILinkToObject.name
    :type: str

    Returns a name of linked object.

.. py:property:: linked_object
    :canonical: ansys.stk.core.stkobjects.ILinkToObject.linked_object
    :type: IAgStkObject

    Dereferences the link and returns the linked object.

.. py:property:: available_objects
    :canonical: ansys.stk.core.stkobjects.ILinkToObject.available_objects
    :type: list

    Returns a list of available objects that can be linked to.

.. py:property:: is_intrinsic
    :canonical: ansys.stk.core.stkobjects.ILinkToObject.is_intrinsic
    :type: bool

    Returns true if the link references an intrinsic object, otherwise returns false.


Method detail
-------------



.. py:method:: bind_to(self, path: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.ILinkToObject.bind_to

    Binds to existing object instance using the specified object path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`



