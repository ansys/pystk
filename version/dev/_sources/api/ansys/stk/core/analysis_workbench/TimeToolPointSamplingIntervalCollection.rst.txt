TimeToolPointSamplingIntervalCollection
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection

   A collection of intervals where each interval contains the time, position and velocity arrays.

.. py:currentmodule:: TimeToolPointSamplingIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection.item`
              - Access an element at the specified position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection.count`
              - Number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolPointSamplingIntervalCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection.count
    :type: int

    Number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> TimeToolPointSamplingInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection.item

    Access an element at the specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TimeToolPointSamplingInterval`


