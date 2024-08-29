CoverageBoundsLatLine
=====================

.. py:class:: ansys.stk.core.stkobjects.CoverageBoundsLatLine

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`

   Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

.. py:currentmodule:: CoverageBoundsLatLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatLine.start_longitude`
              - Longitude at which the latitude line begins. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatLine.stop_longitude`
              - Longitude at which the latitude line ends. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatLine.latitude`
              - Latitude of the latitude line. Uses Latitude Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBoundsLatLine


Property detail
---------------

.. py:property:: start_longitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatLine.start_longitude
    :type: typing.Any

    Longitude at which the latitude line begins. Uses Longitude Dimension.

.. py:property:: stop_longitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatLine.stop_longitude
    :type: typing.Any

    Longitude at which the latitude line ends. Uses Longitude Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatLine.latitude
    :type: typing.Any

    Latitude of the latitude line. Uses Latitude Dimension.


