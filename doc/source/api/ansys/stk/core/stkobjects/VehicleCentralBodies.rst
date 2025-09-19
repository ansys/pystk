VehicleCentralBodies
====================

.. py:class:: ansys.stk.core.stkobjects.VehicleCentralBodies

   Satellite Central Bodies.

.. py:currentmodule:: VehicleCentralBodies

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.assign_central_body`
              - Assign a central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.is_central_body_assigned`
              - Check whether a central body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.remove_all`
              - Remove all the central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.remove_central_body`
              - Remove a central body.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.assigned_central_bodies`
              - Return an array of all assigned central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCentralBodies.available_central_bodies`
              - Return an array of available Central Bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleCentralBodies


Property detail
---------------

.. py:property:: assigned_central_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.assigned_central_bodies
    :type: list

    Return an array of all assigned central bodies.

.. py:property:: available_central_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.available_central_bodies
    :type: list

    Return an array of available Central Bodies.


Method detail
-------------

.. py:method:: assign_central_body(self, central_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.assign_central_body

    Assign a central body.

    :Parameters:

        **central_body** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: is_central_body_assigned(self, central_body: str) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.is_central_body_assigned

    Check whether a central body is already assigned.

    :Parameters:

        **central_body** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.remove_all

    Remove all the central bodies.

    :Returns:

        :obj:`~None`

.. py:method:: remove_central_body(self, central_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleCentralBodies.remove_central_body

    Remove a central body.

    :Parameters:

        **central_body** : :obj:`~str`


    :Returns:

        :obj:`~None`

