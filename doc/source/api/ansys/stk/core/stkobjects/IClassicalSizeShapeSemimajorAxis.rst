IClassicalSizeShapeSemimajorAxis
================================

.. py:class:: ansys.stk.core.stkobjects.IClassicalSizeShapeSemimajorAxis

   IClassicalSizeShape
   
   Interface for specifying orbit size and shape using Semimajor Axis and Eccentricity.

.. py:currentmodule:: IClassicalSizeShapeSemimajorAxis

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapeSemimajorAxis.semi_major_axis`
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapeSemimajorAxis.eccentricity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalSizeShapeSemimajorAxis


Property detail
---------------

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeSemimajorAxis.semi_major_axis
    :type: float

    Half the length of the major (longest) axis of the orbital ellipse. Uses Distance Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeSemimajorAxis.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.


