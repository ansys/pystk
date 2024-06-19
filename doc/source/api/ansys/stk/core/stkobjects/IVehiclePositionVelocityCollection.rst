IVehiclePositionVelocityCollection
==================================

.. py:class:: IVehiclePositionVelocityCollection

   object
   
   An initial state error covariance matrix used to represent the uncertainty in the vehicle's position and velocity. Because the matrix is symmetric, you only need to enter the lower triangle of the 6x6 matrix.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePositionVelocityCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehiclePositionVelocityCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehiclePositionVelocityCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehiclePositionVelocityElement
    :canonical: ansys.stk.core.stkobjects.IVehiclePositionVelocityCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehiclePositionVelocityElement`


