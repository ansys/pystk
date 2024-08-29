BURNOUT_TYPE
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.BURNOUT_TYPE

   IntEnum


.. py:currentmodule:: BURNOUT_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~GEOCENTRIC`
              - Geocentric (Planetocentric) - the burnout point is measured from the center of mass of the Earth or other central body.

            * - :py:attr:`~GEODETIC`
              - Geodetic (Planetodetic) - the burnout point is measured along the normal to the surface of an ellipsoid defined with reference to the Earth (or other central body).

            * - :py:attr:`~LAUNCH_AZIMUTH_RADIUS`
              - Launch Az / Radius - the burnout point is defined in reference to distance downrange along an azimuth, measured from the center of mass of the Earth or other central body.

            * - :py:attr:`~LAUNCH_AZIMUTH_ALTITUDE`
              - Launch Az / Alt - the burnout point is defined in reference to distance downrange along an azimuth, measured from the surface of the Earth or other central body.

            * - :py:attr:`~CBF_CARTESIAN`
              - Central Body Fixed Cartesian - the burnout state is specified in the central-body-fixed Cartesian coordinate system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BURNOUT_TYPE


