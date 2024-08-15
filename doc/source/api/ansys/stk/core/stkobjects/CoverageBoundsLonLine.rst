CoverageBoundsLonLine
=====================

.. py:class:: ansys.stk.core.stkobjects.CoverageBoundsLonLine

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`

   Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

.. py:currentmodule:: CoverageBoundsLonLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLonLine.min_latitude`
              - Minimum latitude used to define the longitude line. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLonLine.max_latitude`
              - Maximum latitude used to define the longitude line. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLonLine.longitude`
              - Longitude of the meridian defining the longitude line. Uses Longitude Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBoundsLonLine


Property detail
---------------

.. py:property:: min_latitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLonLine.min_latitude
    :type: typing.Any

    Minimum latitude used to define the longitude line. Uses Latitude Dimension.

.. py:property:: max_latitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLonLine.max_latitude
    :type: typing.Any

    Maximum latitude used to define the longitude line. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLonLine.longitude
    :type: typing.Any

    Longitude of the meridian defining the longitude line. Uses Longitude Dimension.


