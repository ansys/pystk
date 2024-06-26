IClassicalSizeShapePeriod
=========================

.. py:class:: ansys.stk.core.stkobjects.IClassicalSizeShapePeriod

   IClassicalSizeShape
   
   Interface for specifying orbit size and shape using Period and Eccentricity.

.. py:currentmodule:: IClassicalSizeShapePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapePeriod.period`
              - Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapePeriod.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalSizeShapePeriod


Property detail
---------------

.. py:property:: period
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapePeriod.period
    :type: float

    Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapePeriod.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


