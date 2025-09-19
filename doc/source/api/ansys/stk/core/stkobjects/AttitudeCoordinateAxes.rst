AttitudeCoordinateAxes
======================

.. py:class:: ansys.stk.core.stkobjects.AttitudeCoordinateAxes

   IntEnum


.. py:currentmodule:: AttitudeCoordinateAxes

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CUSTOM`
              - Custom reference axes.

            * - :py:attr:`~FIXED`
              - The Fixed frame of a central body is the frame in which its topography is expressed.

            * - :py:attr:`~J2000`
              - Mean Equator and Mean Equinox of the J2000 epoch (JD 2451545.0 TDB which is 1 Jan 2000 12:00:00.000 TDB). The J2000 axes were considered the best realized inertial axes until the development of the ICRF.

            * - :py:attr:`~ICRF`
              - International Celestial Reference Frame. The ICRF axes are defined as the inertial (i.e., kinematically non-rotating) axes associated with a general relativity frame centered at the solar system barycenter (often called the BCRF).

            * - :py:attr:`~INERTIAL`
              - Each central body defines its own Inertial frame computed as a constant rotation from the ICRF frame. Earth and Sun both define their Inertial frames as ICRF itself (i.e., no rotation) and do not provide an additional frame named Inertial.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeCoordinateAxes


