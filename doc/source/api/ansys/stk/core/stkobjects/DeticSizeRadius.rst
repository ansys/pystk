DeticSizeRadius
===============

.. py:class:: ansys.stk.core.stkobjects.DeticSizeRadius

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`

   Radius and Radius Rate (for Geodetic coordinate type).

.. py:currentmodule:: DeticSizeRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DeticSizeRadius.radius`
              - Measured from the center of the Earth. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DeticSizeRadius.rate`
              - Rate of change in radius. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DeticSizeRadius


Property detail
---------------

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.DeticSizeRadius.radius
    :type: float

    Measured from the center of the Earth. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.DeticSizeRadius.rate
    :type: float

    Rate of change in radius. Uses Rate Dimension.


