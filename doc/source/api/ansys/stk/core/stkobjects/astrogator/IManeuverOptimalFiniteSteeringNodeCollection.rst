IManeuverOptimalFiniteSteeringNodeCollection
============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection

   object
   
   Steering/nodes collection.

.. py:currentmodule:: IManeuverOptimalFiniteSteeringNodeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverOptimalFiniteSteeringNodeCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IManeuverOptimalFiniteSteeringNodeElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IManeuverOptimalFiniteSteeringNodeElement`



