ElementSphericalRangeRate
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Spherical Range Rate elements.

.. py:currentmodule:: ElementSphericalRangeRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.right_ascension`
              - Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.declination`
              - Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.range`
              - The magnitude of the satellite position vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.right_ascension_rate`
              - The rate of change of the right ascension. Uses Angle Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.declination_rate`
              - The rate of change of the declination. Uses Angle Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.range_rate`
              - The rate of change of the range. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementSphericalRangeRate


Property detail
---------------

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.right_ascension
    :type: typing.Any

    Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.declination
    :type: typing.Any

    Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.range
    :type: float

    The magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: right_ascension_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.right_ascension_rate
    :type: float

    The rate of change of the right ascension. Uses Angle Rate Dimension.

.. py:property:: declination_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.declination_rate
    :type: float

    The rate of change of the declination. Uses Angle Rate Dimension.

.. py:property:: range_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate.range_rate
    :type: float

    The rate of change of the range. Uses Rate Dimension.


