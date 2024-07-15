OnePointAccessConstraintCollection
==================================

.. py:class:: ansys.stk.core.stkobjects.OnePointAccessConstraintCollection

   Bases: 

   Represents the access constraints for the one point access computation.

.. py:currentmodule:: OnePointAccessConstraintCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessConstraintCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessConstraintCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessConstraintCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OnePointAccessConstraintCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.OnePointAccessConstraintCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.OnePointAccessConstraintCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> OnePointAccessConstraint
    :canonical: ansys.stk.core.stkobjects.OnePointAccessConstraintCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~OnePointAccessConstraint`


