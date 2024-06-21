ICentralBodyAttitudeIAU1994
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994

   ICentralBodyAttitude
   
   Properties for an IAU1994 attitude definition.

.. py:currentmodule:: ICentralBodyAttitudeIAU1994

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.right_ascension`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.declination`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.right_ascension_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.declination_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.rotation_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.rotation_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICentralBodyAttitudeIAU1994


Property detail
---------------

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.right_ascension
    :type: typing.Any

    Gets or sets the right ascension; the angle measured in the inertial equatorial plane from the inertial X axis in a right-handed sense about the inertial Z axis to the spin axis -- the angle  in the drawing below. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.declination
    :type: typing.Any

    Gets or sets the declination; the angle from the X-Y plane of the coordinate system to the spin axis vector. Uses Angle Dimension.

.. py:property:: right_ascension_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.right_ascension_rate
    :type: float

    Gets or sets the right ascension rate; the rate of change in the right ascension. Uses AngleRate Dimension.

.. py:property:: declination_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.declination_rate
    :type: float

    Gets or sets the declination rate; the rate of change in the declination. Uses AngleRate Dimension.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.rotation_offset
    :type: typing.Any

    Gets or sets the rotation offset; the angle from the inertially fixed reference direction to the body-fixed prime meridian (0 deg longitude) at the time of epoch. Uses AngleUnit Dimension.

.. py:property:: rotation_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994.rotation_rate
    :type: float

    Gets or sets the rotation rate; the rate of the central body's rotation. Uses AngleRate Dimension.


