ElementSetType
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementSetType

   IntEnum


.. py:currentmodule:: ElementSetType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CARTESIAN`
              - Cartesian - specifying an orbit by three position elements and three velocity elements in a rectangular coordinate system.

            * - :py:attr:`~KEPLERIAN`
              - Keplerian - the classical system, specifying an orbit by six elements describing its size, shape and three-dimensional orientation in space.

            * - :py:attr:`~SPHERICAL`
              - Spherical - a system in which positions are specified as a radial distance from the origin and two angles relative to a fundamental plane.

            * - :py:attr:`~TARGET_VECTOR_INCOMING_ASYMPTOTE`
              - Target Vector Incoming Asymptote - used for hyperbolic arrival trajectories.

            * - :py:attr:`~TARGET_VECTOR_OUTGOING_ASYMPTOTE`
              - Target Vector Outgoing Asymptote - used for hyperbolic departure trajectories.

            * - :py:attr:`~MIXED_SPHERICAL`
              - Mixed Spherical.

            * - :py:attr:`~DELAUNAY`
              - Delaunay.

            * - :py:attr:`~EQUINOCTIAL`
              - Equinoctial.

            * - :py:attr:`~GEODETIC`
              - Geodetic.

            * - :py:attr:`~B_PLANE`
              - BPlane.

            * - :py:attr:`~SPHERICAL_RANGE_RATE`
              - Spherical Range Rate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementSetType


