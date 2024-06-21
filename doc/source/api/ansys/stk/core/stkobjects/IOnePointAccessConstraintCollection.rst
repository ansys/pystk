IOnePointAccessConstraintCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection

   object
   
   Represents the access constraints for the one point access computation.

.. py:currentmodule:: IOnePointAccessConstraintCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOnePointAccessConstraintCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IOnePointAccessConstraint
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraintCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IOnePointAccessConstraint`


