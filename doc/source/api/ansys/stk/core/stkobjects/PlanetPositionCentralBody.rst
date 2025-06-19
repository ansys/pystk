PlanetPositionCentralBody
=========================

.. py:class:: ansys.stk.core.stkobjects.PlanetPositionCentralBody

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPositionSourceData`

   Class defining central body used to define Planet object.

.. py:currentmodule:: PlanetPositionCentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.central_body`
              - The central body used in defining the planet object.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.rename_automatically`
              - Specify whether the object should automatically be renamed to have the same name as the selected central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.radius`
              - The radius of the selected central body. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.ephemeris_source`
              - The ephemeris source for the selected central body. A member of the EphemSourceType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.available_central_bodies`
              - Return an array of all available Central Bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.available_ephemeris_source_types`
              - Return an array of all available Ephemeris Source Types.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody.jplde_version`
              - Return a JPL DE Version.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlanetPositionCentralBody


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.central_body
    :type: str

    The central body used in defining the planet object.

.. py:property:: rename_automatically
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.rename_automatically
    :type: bool

    Specify whether the object should automatically be renamed to have the same name as the selected central body.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.radius
    :type: float

    The radius of the selected central body. Uses Distance Dimension.

.. py:property:: ephemeris_source
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.ephemeris_source
    :type: EphemSourceType

    The ephemeris source for the selected central body. A member of the EphemSourceType enumeration.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.available_central_bodies
    :type: list

    Return an array of all available Central Bodies.

.. py:property:: available_ephemeris_source_types
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.available_ephemeris_source_types
    :type: list

    Return an array of all available Ephemeris Source Types.

.. py:property:: jplde_version
    :canonical: ansys.stk.core.stkobjects.PlanetPositionCentralBody.jplde_version
    :type: str

    Return a JPL DE Version.


