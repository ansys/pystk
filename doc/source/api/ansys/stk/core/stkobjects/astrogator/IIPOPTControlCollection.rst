IIPOPTControlCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection

   object
   
   Properties for the list of IPOPT control parameters.

.. py:currentmodule:: IIPOPTControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.count`
              - Returns the size of the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IIPOPTControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IIPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IIPOPTControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IIPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IIPOPTControl`

