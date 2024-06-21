ICoverageGridPointSelection
===========================

.. py:class:: ansys.stk.core.stkobjects.ICoverageGridPointSelection

   object
   
   Represents a set of coverage grid points.

.. py:currentmodule:: ICoverageGridPointSelection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGridPointSelection.to_array`
              - Return a jagged array of grid points and their intervals. The elements are single-dimension arrays each containing three elements: latitude, longitude and a jagged array of access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGridPointSelection.item`
              - Given an index, returns a point in the selection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGridPointSelection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGridPointSelection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGridPointSelection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICoverageGridPointSelection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator object.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICoverageGridPointSelection.count
    :type: int

    Returns the number of points in the selection.


Method detail
-------------


.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.ICoverageGridPointSelection.to_array

    Return a jagged array of grid points and their intervals. The elements are single-dimension arrays each containing three elements: latitude, longitude and a jagged array of access intervals.

    :Returns:

        :obj:`~list`


.. py:method:: item(self, index: int) -> ICoverageSelectedGridPoint
    :canonical: ansys.stk.core.stkobjects.ICoverageGridPointSelection.item

    Given an index, returns a point in the selection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICoverageSelectedGridPoint`

