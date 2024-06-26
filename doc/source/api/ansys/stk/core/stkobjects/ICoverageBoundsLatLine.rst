ICoverageBoundsLatLine
======================

.. py:class:: ansys.stk.core.stkobjects.ICoverageBoundsLatLine

   ICoverageBounds
   
   Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

.. py:currentmodule:: ICoverageBoundsLatLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLatLine.start_longitude`
              - Longitude at which the latitude line begins. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLatLine.stop_longitude`
              - Longitude at which the latitude line ends. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLatLine.latitude`
              - Latitude of the latitude line. Uses Latitude Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageBoundsLatLine


Property detail
---------------

.. py:property:: start_longitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLine.start_longitude
    :type: typing.Any

    Longitude at which the latitude line begins. Uses Longitude Dimension.

.. py:property:: stop_longitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLine.stop_longitude
    :type: typing.Any

    Longitude at which the latitude line ends. Uses Longitude Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLine.latitude
    :type: typing.Any

    Latitude of the latitude line. Uses Latitude Dimension.


