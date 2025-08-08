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

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.assign_eclipsing_body`
              - Add an eclipsing body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.is_eclipsing_body_assigned`
              - Return true if the eclipsing body is assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_all_eclipsing_bodies`
              - Remove all eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_eclipsing_body`
              - Remove an eclipsing body.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.assigned_eclipsing_bodies`
              - Get the assigned eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies.available_eclipsing_bodies`
              - Get the available eclipsing bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEclipsingBodies


Property detail
---------------

.. py:property:: assigned_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.assigned_eclipsing_bodies
    :type: list

    Get the assigned eclipsing bodies.

.. py:property:: available_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.available_eclipsing_bodies
    :type: list

    Get the available eclipsing bodies.


Method detail
-------------

.. py:method:: assign_eclipsing_body(self, eclipsing_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.assign_eclipsing_body

    Add an eclipsing body.

    :Parameters:

        **eclipsing_body** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: is_eclipsing_body_assigned(self, eclipsing_body: str) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.is_eclipsing_body_assigned

    Return true if the eclipsing body is assigned.

    :Parameters:

        **eclipsing_body** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: remove_all_eclipsing_bodies(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_all_eclipsing_bodies

    Remove all eclipsing bodies.

    :Returns:

        :obj:`~None`

.. py:method:: remove_eclipsing_body(self, eclipsing_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEclipsingBodies.remove_eclipsing_body

    Remove an eclipsing body.

    :Parameters:

        **eclipsing_body** : :obj:`~str`


    :Returns:

        :obj:`~None`

