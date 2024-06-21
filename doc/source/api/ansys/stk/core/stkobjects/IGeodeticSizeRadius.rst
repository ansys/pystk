IGeodeticSizeRadius
===================

.. py:class:: ansys.stk.core.stkobjects.IGeodeticSizeRadius

   IGeodeticSize
   
   Interface for Radius and Radius Rate (for Geodetic coordinate type).

.. py:currentmodule:: IGeodeticSizeRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGeodeticSizeRadius.radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGeodeticSizeRadius.rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGeodeticSizeRadius


Property detail
---------------

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IGeodeticSizeRadius.radius
    :type: float

    Measured from the center of the Earth. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.IGeodeticSizeRadius.rate
    :type: float

    Rate of change in radius. Uses Rate Dimension.


