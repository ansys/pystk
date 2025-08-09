ClassicalSizeShapeMeanMotion
============================

.. py:class:: ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion

   Bases: :py:class:`~ansys.stk.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Mean Motion and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapeMeanMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion.mean_motion`
              - Identifies the number of orbits per day (86400 sec/period), based on assumed two-body motion. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ClassicalSizeShapeMeanMotion


Property detail
---------------

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion.mean_motion
    :type: float

    Identifies the number of orbits per day (86400 sec/period), based on assumed two-body motion. Uses AngleRate Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


