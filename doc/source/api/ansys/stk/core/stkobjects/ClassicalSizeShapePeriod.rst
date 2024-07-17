ClassicalSizeShapePeriod
========================

.. py:class:: ansys.stk.core.stkobjects.ClassicalSizeShapePeriod

   Bases: :py:class:`~ansys.stk.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Period and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapePeriod.period`
              - Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapePeriod.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ClassicalSizeShapePeriod


Property detail
---------------

.. py:property:: period
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapePeriod.period
    :type: float

    Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapePeriod.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


