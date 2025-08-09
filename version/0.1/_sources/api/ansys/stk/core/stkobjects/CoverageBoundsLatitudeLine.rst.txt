CoverageBoundsLatitudeLine
==========================

.. py:class:: ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`

   Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

.. py:currentmodule:: CoverageBoundsLatitudeLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.start_longitude`
              - Longitude at which the latitude line begins. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.stop_longitude`
              - Longitude at which the latitude line ends. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.latitude`
              - Latitude of the latitude line. Uses Latitude Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBoundsLatitudeLine


Property detail
---------------

.. py:property:: start_longitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.start_longitude
    :type: typing.Any

    Longitude at which the latitude line begins. Uses Longitude Dimension.

.. py:property:: stop_longitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.stop_longitude
    :type: typing.Any

    Longitude at which the latitude line ends. Uses Longitude Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine.latitude
    :type: typing.Any

    Latitude of the latitude line. Uses Latitude Dimension.


