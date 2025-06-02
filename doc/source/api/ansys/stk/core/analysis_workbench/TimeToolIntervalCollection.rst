TimeToolIntervalCollection
==========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolIntervalCollection

   Represents a collection of intervals.

.. py:currentmodule:: TimeToolIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolIntervalCollection.item`
              - Return an interval at a specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolIntervalCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolIntervalCollection._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolIntervalCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolIntervalCollection._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> TimeToolInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolIntervalCollection.item

    Return an interval at a specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TimeToolInterval`


