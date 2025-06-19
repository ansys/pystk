TimeToolAxesSamplingIntervalCollection
======================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection

   A collection of intervals where each interval contains the time, orientation and velocity arrays.

.. py:currentmodule:: TimeToolAxesSamplingIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection.item`
              - Access an element at the specified position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection.count`
              - Number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolAxesSamplingIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection.count
    :type: int

    Number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> TimeToolAxesSamplingInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection.item

    Access an element at the specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TimeToolAxesSamplingInterval`


