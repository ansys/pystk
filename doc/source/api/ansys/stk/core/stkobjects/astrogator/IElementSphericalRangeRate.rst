IElementSphericalRangeRate
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate

   IElement
   
   Properties for Spherical Range Rate elements.

.. py:currentmodule:: IElementSphericalRangeRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.right_ascension`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.declination`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.range`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.right_ascension_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.declination_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.range_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementSphericalRangeRate


Property detail
---------------

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.right_ascension
    :type: typing.Any

    Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.declination
    :type: typing.Any

    Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.range
    :type: float

    The magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: right_ascension_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.right_ascension_rate
    :type: float

    The rate of change of the right ascension. Uses Angle Rate Dimension.

.. py:property:: declination_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.declination_rate
    :type: float

    The rate of change of the declination. Uses Angle Rate Dimension.

.. py:property:: range_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate.range_rate
    :type: float

    The rate of change of the range. Uses Rate Dimension.


