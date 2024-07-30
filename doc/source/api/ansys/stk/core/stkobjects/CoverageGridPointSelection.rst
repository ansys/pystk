CoverageGridPointSelection
==========================

.. py:class:: ansys.stk.core.stkobjects.CoverageGridPointSelection

   Bases: 

   Represents a set of points selected with the grid inspector.

.. py:currentmodule:: CoverageGridPointSelection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridPointSelection.to_array`
              - Return a jagged array of grid points and their intervals. The elements are single-dimension arrays each containing three elements: latitude, longitude and a jagged array of access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridPointSelection.item`
              - Given an index, returns a point in the selection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridPointSelection._NewEnum`
              - Returns a COM enumerator object.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridPointSelection.count`
              - Returns the number of points in the selection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGridPointSelection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.CoverageGridPointSelection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator object.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CoverageGridPointSelection.count
    :type: int

    Returns the number of points in the selection.


Method detail
-------------


.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.CoverageGridPointSelection.to_array

    Return a jagged array of grid points and their intervals. The elements are single-dimension arrays each containing three elements: latitude, longitude and a jagged array of access intervals.

    :Returns:

        :obj:`~list`


.. py:method:: item(self, index: int) -> CoverageSelectedGridPoint
    :canonical: ansys.stk.core.stkobjects.CoverageGridPointSelection.item

    Given an index, returns a point in the selection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CoverageSelectedGridPoint`

