IAccessConstraintCentralBodyObstruction
=======================================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction

   IAccessConstraint
   
   Access Constraint used for Central Body Obstruction.

.. py:currentmodule:: IAccessConstraintCentralBodyObstruction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.is_obstruction_assigned`
              - Check whether a central body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.add_obstruction`
              - Add a Central Body Obstruction by Name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.remove_obstruction`
              - Remove a Central Body Obstruction by Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.assigned_obstructions`
              - Gets the Assigned Obstructions.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.available_obstructions`
              - Gets the Available Obstructions.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintCentralBodyObstruction


Property detail
---------------

.. py:property:: assigned_obstructions
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.assigned_obstructions
    :type: list

    Gets the Assigned Obstructions.

.. py:property:: available_obstructions
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.available_obstructions
    :type: list

    Gets the Available Obstructions.


Method detail
-------------


.. py:method:: is_obstruction_assigned(self, obstruction: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.is_obstruction_assigned

    Check whether a central body is already assigned.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.add_obstruction

    Add a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCentralBodyObstruction.remove_obstruction

    Remove a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`


