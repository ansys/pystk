ITimeToolAxesSamplingIntervalCollection
=======================================

.. py:class:: ITimeToolAxesSamplingIntervalCollection

   object
   
   A collection of intervals where each interval contains the time, orientation and velocity arrays.

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

    from ansys.stk.core.vgt import ITimeToolAxesSamplingIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingIntervalCollection.count
    :type: int

    Number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingIntervalCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index:int) -> "ITimeToolAxesSamplingInterval"

    Access an element at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ITimeToolAxesSamplingInterval"`


