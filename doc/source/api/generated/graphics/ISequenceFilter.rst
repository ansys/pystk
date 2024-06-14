ISequenceFilter
===============

.. py:class:: ISequenceFilter

   object
   
   Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a filter to the sequence.
            * - :py:meth:`~remove`
              - Remove a filter from the sequence.
            * - :py:meth:`~clear`
              - Clear all filters from the sequence.
            * - :py:meth:`~contains`
              - Return true if the sequence contains the filter.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~continue_on_failure`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISequenceFilter


Property detail
---------------

.. py:property:: continue_on_failure
    :canonical: ansys.stk.core.graphics.ISequenceFilter.continue_on_failure
    :type: bool

    Gets or sets whether to continue applying filters in the sequence regardless of individual filter failures. When set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ISequenceFilter.count
    :type: int

    Gets the number of filters in the collection.


Method detail
-------------




.. py:method:: add(self, filter:"IRasterFilter") -> None

    Add a filter to the sequence.

    :Parameters:

    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, filter:"IRasterFilter") -> None

    Remove a filter from the sequence.

    :Parameters:

    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None

    Clear all filters from the sequence.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, filter:"IRasterFilter") -> bool

    Return true if the sequence contains the filter.

    :Parameters:

    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~bool`

