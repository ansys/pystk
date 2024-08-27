GeodeticSizeRadius
==================

.. py:class:: ansys.stk.core.stkobjects.GeodeticSizeRadius

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`

   Radius and Radius Rate (for Geodetic coordinate type).

.. py:currentmodule:: GeodeticSizeRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.GeodeticSizeRadius.radius`
              - Measured from the center of the Earth. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GeodeticSizeRadius.rate`
              - Rate of change in radius. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import GeodeticSizeRadius


Property detail
---------------

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.GeodeticSizeRadius.radius
    :type: float

    Measured from the center of the Earth. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.GeodeticSizeRadius.rate
    :type: float

    Rate of change in radius. Uses Rate Dimension.


