IVehicleEclipsingBodies
=======================

.. py:class:: IVehicleEclipsingBodies

   object
   
   Interface for eclipsing bodies.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_eclipsing_body_assigned`
              - Return true if the eclipsing body is assigned.
            * - :py:meth:`~assign_eclipsing_body`
              - Add an eclipsing body.
            * - :py:meth:`~remove_eclipsing_body`
              - Remove an eclipsing body.
            * - :py:meth:`~remove_all_eclipsing_bodies`
              - Remove all eclipsing bodies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_eclipsing_bodies`
            * - :py:meth:`~assigned_eclipsing_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEclipsingBodies


Property detail
---------------

.. py:property:: available_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleEclipsingBodies.available_eclipsing_bodies
    :type: list

    Gets the available eclipsing bodies.

.. py:property:: assigned_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleEclipsingBodies.assigned_eclipsing_bodies
    :type: list

    Gets the assigned eclipsing bodies.


Method detail
-------------



.. py:method:: is_eclipsing_body_assigned(self, eclipsingBody:str) -> bool

    Return true if the eclipsing body is assigned.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: assign_eclipsing_body(self, eclipsingBody:str) -> None

    Add an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_eclipsing_body(self, eclipsingBody:str) -> None

    Remove an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_eclipsing_bodies(self) -> None

    Remove all eclipsing bodies.

    :Returns:

        :obj:`~None`

