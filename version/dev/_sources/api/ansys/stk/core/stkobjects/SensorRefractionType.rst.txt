SensorRefractionType
====================

.. py:class:: ansys.stk.core.stkobjects.SensorRefractionType

   IntEnum


.. py:currentmodule:: SensorRefractionType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EARTH_FOUR_THIRDS_RADIUS_METHOD`
              - 4/3 Earth Radius: computes the apparent elevation due to refraction by assuming an Earth radius 4/3 of its actual value.

            * - :py:attr:`~SCF_METHOD`
              - SCF Method: an implementation of the Refraction Correction model,which takes as input the surface refractivity at each facility location, based on local temperature, pressure and humidity, correcting elevation and range from apparent to true.

            * - :py:attr:`~ITU_R_P834_4`
              - ITU-R P.834-4: Compute the refracted elevation based on the non-refracted elevation angle and the mean sea level (MSL) altitude of the sensor, using empirical criteria that are contained in ITU-R P.834-4.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorRefractionType


