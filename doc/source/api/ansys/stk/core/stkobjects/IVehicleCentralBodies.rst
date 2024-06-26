IVehicleCentralBodies
=====================

.. py:class:: ansys.stk.core.stkobjects.IVehicleCentralBodies

   object
   
   Satellite Central Bodies interface.

.. py:currentmodule:: IVehicleCentralBodies

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.is_central_body_assigned`
              - Check whether a central body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.assign_central_body`
              - Assign a central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.remove_central_body`
              - Remove a central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.remove_all`
              - Remove all the central bodies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.available_central_bodies`
              - Returns an array of available Central Bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleCentralBodies.assigned_central_bodies`
              - Returns an array of all assigned central bodies.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleCentralBodies


Property detail
---------------

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.available_central_bodies
    :type: list

    Returns an array of available Central Bodies.

.. py:property:: assigned_central_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.assigned_central_bodies
    :type: list

    Returns an array of all assigned central bodies.


Method detail
-------------


.. py:method:: is_central_body_assigned(self, centralBody: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.is_central_body_assigned

    Check whether a central body is already assigned.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~bool`


.. py:method:: assign_central_body(self, centralBody: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.assign_central_body

    Assign a central body.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_central_body(self, centralBody: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.remove_central_body

    Remove a central body.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleCentralBodies.remove_all

    Remove all the central bodies.

    :Returns:

        :obj:`~None`

