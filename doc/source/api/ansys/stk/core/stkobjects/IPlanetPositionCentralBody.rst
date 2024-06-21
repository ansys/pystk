IPlanetPositionCentralBody
==========================

.. py:class:: ansys.stk.core.stkobjects.IPlanetPositionCentralBody

   object
   
   IAgPlPosCentralBody Interface.

.. py:currentmodule:: IPlanetPositionCentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.central_body`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.auto_rename`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.ephem_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.available_central_bodies`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.available_ephem_source_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetPositionCentralBody.jplde_version`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlanetPositionCentralBody


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.central_body
    :type: str

    The central body used in defining the planet object.

.. py:property:: auto_rename
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.auto_rename
    :type: bool

    Specify whether the object should automatically be renamed to have the same name as the selected central body.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.radius
    :type: float

    The radius of the selected central body. Uses Distance Dimension.

.. py:property:: ephem_source
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.ephem_source
    :type: EPHEM_SOURCE_TYPE

    The ephemeris source for the selected central body. A member of the AgEEphemSourceType enumeration.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.available_central_bodies
    :type: list

    Returns an array of all available Central Bodies.

.. py:property:: available_ephem_source_types
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.available_ephem_source_types
    :type: list

    Returns an array of all available Ephemeris Source Types.

.. py:property:: jplde_version
    :canonical: ansys.stk.core.stkobjects.IPlanetPositionCentralBody.jplde_version
    :type: str

    Returns a JPL DE Version.


