SequenceFilter
==============

.. py:class:: ansys.stk.core.graphics.SequenceFilter

   Bases: :py:class:`~ansys.stk.core.graphics.IRasterFilter`

   Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

.. py:currentmodule:: SequenceFilter

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.add`
              - Add a filter to the sequence.
            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.remove`
              - Remove a filter from the sequence.
            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.clear`
              - Clear all filters from the sequence.
            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.contains`
              - Return true if the sequence contains the filter.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.continue_on_failure`
              - Get or set whether to continue applying filters in the sequence regardless of individual filter failures. When set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.
            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilter.count`
              - Get the number of filters in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SequenceFilter


Property detail
---------------

.. py:property:: continue_on_failure
    :canonical: ansys.stk.core.graphics.SequenceFilter.continue_on_failure
    :type: bool

    Get or set whether to continue applying filters in the sequence regardless of individual filter failures. When set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

.. py:property:: count
    :canonical: ansys.stk.core.graphics.SequenceFilter.count
    :type: int

    Get the number of filters in the collection.


Method detail
-------------




.. py:method:: add(self, filter: IRasterFilter) -> None
    :canonical: ansys.stk.core.graphics.SequenceFilter.add

    Add a filter to the sequence.

    :Parameters:

        **filter** : :obj:`~IRasterFilter`


    :Returns:

        :obj:`~None`

.. py:method:: remove(self, filter: IRasterFilter) -> None
    :canonical: ansys.stk.core.graphics.SequenceFilter.remove

    Remove a filter from the sequence.

    :Parameters:

        **filter** : :obj:`~IRasterFilter`


    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.SequenceFilter.clear

    Clear all filters from the sequence.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, filter: IRasterFilter) -> bool
    :canonical: ansys.stk.core.graphics.SequenceFilter.contains

    Return true if the sequence contains the filter.

    :Parameters:

        **filter** : :obj:`~IRasterFilter`


    :Returns:

        :obj:`~bool`

