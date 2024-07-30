IPOPTControlCollection
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection

   Bases: 

   Properties for the list of IPOPT control parameters.

.. py:currentmodule:: IPOPTControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IPOPTControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IPOPTControl`

