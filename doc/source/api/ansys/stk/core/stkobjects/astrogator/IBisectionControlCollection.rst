IBisectionControlCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection

   object
   
   Properties for the list of Bisection control parameters.

.. py:currentmodule:: IBisectionControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.count`
              - Returns the size of the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBisectionControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IBisectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IBisectionControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IBisectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IBisectionControl`

