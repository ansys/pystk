BisectionControlCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.BisectionControlCollection

   Bisection control collection.

.. py:currentmodule:: BisectionControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BisectionControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> BisectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~BisectionControl`



.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> BisectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~BisectionControl`

