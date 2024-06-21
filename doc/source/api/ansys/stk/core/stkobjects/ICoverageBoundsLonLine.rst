ICoverageBoundsLonLine
======================

.. py:class:: ansys.stk.core.stkobjects.ICoverageBoundsLonLine

   ICoverageBounds
   
   Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

.. py:currentmodule:: ICoverageBoundsLonLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLonLine.min_latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLonLine.max_latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsLonLine.longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageBoundsLonLine


Property detail
---------------

.. py:property:: min_latitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLonLine.min_latitude
    :type: typing.Any

    Minimum latitude used to define the longitude line. Uses Latitude Dimension.

.. py:property:: max_latitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLonLine.max_latitude
    :type: typing.Any

    Maximum latitude used to define the longitude line. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLonLine.longitude
    :type: typing.Any

    Longitude of the meridian defining the longitude line. Uses Longitude Dimension.


