AttitudeScheduleTimesCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection

   List of scheduled accesses.

.. py:currentmodule:: AttitudeScheduleTimesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.add`
              - Add a new element to the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.available_targets`
              - Return a list of available targets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeScheduleTimesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.available_targets
    :type: list

    Return a list of available targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> AttitudeScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AttitudeScheduleTimesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, target_path: str) -> AttitudeScheduleTimesElement
    :canonical: ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection.add

    Add a new element to the collection.

    :Parameters:

        **target_path** : :obj:`~str`


    :Returns:

        :obj:`~AttitudeScheduleTimesElement`


