LinkToObject
============

.. py:class:: ansys.stk.core.stkobjects.LinkToObject

   Class defining a link to an STK object.

.. py:currentmodule:: LinkToObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LinkToObject.bind_to_object`
              - Binds to existing object instance using the specified object path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LinkToObject.name`
              - Return a name of linked object.
            * - :py:attr:`~ansys.stk.core.stkobjects.LinkToObject.linked_object`
              - Dereferences the link and returns the linked object.
            * - :py:attr:`~ansys.stk.core.stkobjects.LinkToObject.available_objects`
              - Return a list of available objects that can be linked to.
            * - :py:attr:`~ansys.stk.core.stkobjects.LinkToObject.is_intrinsic`
              - Return true if the link references an intrinsic object, otherwise returns false.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LinkToObject


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.LinkToObject.name
    :type: str

    Return a name of linked object.

.. py:property:: linked_object
    :canonical: ansys.stk.core.stkobjects.LinkToObject.linked_object
    :type: ISTKObject

    Dereferences the link and returns the linked object.

.. py:property:: available_objects
    :canonical: ansys.stk.core.stkobjects.LinkToObject.available_objects
    :type: list

    Return a list of available objects that can be linked to.

.. py:property:: is_intrinsic
    :canonical: ansys.stk.core.stkobjects.LinkToObject.is_intrinsic
    :type: bool

    Return true if the link references an intrinsic object, otherwise returns false.


Method detail
-------------



.. py:method:: bind_to_object(self, path: str) -> ISTKObject
    :canonical: ansys.stk.core.stkobjects.LinkToObject.bind_to_object

    Binds to existing object instance using the specified object path.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~ISTKObject`



