IClassicalSizeShapeMeanMotion
=============================

.. py:class:: IClassicalSizeShapeMeanMotion

   IClassicalSizeShape
   
   Interface for specifying orbit size and shape using Mean Motion and Eccentricity.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mean_motion`
            * - :py:meth:`~eccentricity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalSizeShapeMeanMotion


Property detail
---------------

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeMeanMotion.mean_motion
    :type: float

    Identifies the number of orbits per day (86400 sec/period), based on assumed two-body motion. Uses AngleRate Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeMeanMotion.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


