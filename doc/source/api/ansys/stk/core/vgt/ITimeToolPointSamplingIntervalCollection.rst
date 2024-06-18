ITimeToolPointSamplingIntervalCollection
========================================

.. py:class:: ITimeToolPointSamplingIntervalCollection

   object
   
   A collection of intervals where each interval contains the time, position and velocity arrays.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Access an element at the specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolPointSamplingIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolPointSamplingIntervalCollection.count
    :type: int

    Number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolPointSamplingIntervalCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index:int) -> "ITimeToolPointSamplingInterval"

    Access an element at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ITimeToolPointSamplingInterval"`


