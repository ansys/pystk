IVehicleThirdBodyGravityCollection
==================================

.. py:class:: IVehicleThirdBodyGravityCollection

   object
   
   Third Body Gravity Collection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add_third_body`
              - Add a new element to the collection.
            * - :py:meth:`~remove_third_body`
              - Remove an element from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_third_body_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleThirdBodyGravityCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_third_body_names
    :canonical: ansys.stk.core.stkobjects.IVehicleThirdBodyGravityCollection.available_third_body_names
    :type: list

    Gets the available third bodies. The return result is a collection of strings representing names of the central bodies that can be used as third body.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehicleThirdBodyGravityElement"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehicleThirdBodyGravityElement"`


.. py:method:: remove_at(self, index:int) -> None

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`


.. py:method:: add_third_body(self, thirdBody:str) -> "IVehicleThirdBodyGravityElement"

    Add a new element to the collection.

    :Parameters:

    **thirdBody** : :obj:`~str`

    :Returns:

        :obj:`~"IVehicleThirdBodyGravityElement"`

.. py:method:: remove_third_body(self, thirdBody:str) -> None

    Remove an element from the collection.

    :Parameters:

    **thirdBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

