PropagatorHPOPThirdBodyGravityCollection
========================================

.. py:class:: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection

   Collection of third-body gravity options for the LOP propagator.

.. py:currentmodule:: PropagatorHPOPThirdBodyGravityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.add_third_body`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_third_body`
              - Remove an element from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.available_third_body_names`
              - Gets the available third bodies. The return result is a collection of strings representing names of the central bodies that can be used as third body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorHPOPThirdBodyGravityCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_third_body_names
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.available_third_body_names
    :type: list

    Gets the available third bodies. The return result is a collection of strings representing names of the central bodies that can be used as third body.


Method detail
-------------


.. py:method:: item(self, index: int) -> PropagatorHPOPThirdBodyGravityElement
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~PropagatorHPOPThirdBodyGravityElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`


.. py:method:: add_third_body(self, third_body: str) -> PropagatorHPOPThirdBodyGravityElement
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.add_third_body

    Add a new element to the collection.

    :Parameters:

    **third_body** : :obj:`~str`

    :Returns:

        :obj:`~PropagatorHPOPThirdBodyGravityElement`

.. py:method:: remove_third_body(self, third_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection.remove_third_body

    Remove an element from the collection.

    :Parameters:

    **third_body** : :obj:`~str`

    :Returns:

        :obj:`~None`

