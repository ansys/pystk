VehicleEclipsingBodies
======================

.. py:class:: ansys.stk.core.stkobjects.VehicleEclipsingBodies

   Eclipsing bodies.

.. py:currentmodule:: VehicleEclipsingBodies

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.is_eclipsing_body_assigned`
              - Return true if the eclipsing body is assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.assign_eclipsing_body`
              - Add an eclipsing body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_eclipsing_body`
              - Remove an eclipsing body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_all_eclipsing_bodies`
              - Remove all eclipsing bodies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.available_eclipsing_bodies`
              - Gets the available eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.assigned_eclipsing_bodies`
              - Gets the assigned eclipsing bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEclipsingBodies


Property detail
---------------

.. py:property:: available_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.available_eclipsing_bodies
    :type: list

    Gets the available eclipsing bodies.

.. py:property:: assigned_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.assigned_eclipsing_bodies
    :type: list

    Gets the assigned eclipsing bodies.


Method detail
-------------



.. py:method:: is_eclipsing_body_assigned(self, eclipsingBody: str) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.is_eclipsing_body_assigned

    Return true if the eclipsing body is assigned.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: assign_eclipsing_body(self, eclipsingBody: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.assign_eclipsing_body

    Add an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_eclipsing_body(self, eclipsingBody: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_eclipsing_body

    Remove an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_eclipsing_bodies(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_all_eclipsing_bodies

    Remove all eclipsing bodies.

    :Returns:

        :obj:`~None`

