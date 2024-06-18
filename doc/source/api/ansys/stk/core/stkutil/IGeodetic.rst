IGeodetic
=========

.. py:class:: IGeodetic

   IPosition
   
   IAgGeodetic sets the position using Geodetic properties.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~lat`
            * - :py:meth:`~lon`
            * - :py:meth:`~altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IGeodetic


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkutil.IGeodetic.lat
    :type: typing.Any

    Latitude. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkutil.IGeodetic.lon
    :type: typing.Any

    Longitude. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkutil.IGeodetic.altitude
    :type: float

    Altitude. Dimension depends on context.


