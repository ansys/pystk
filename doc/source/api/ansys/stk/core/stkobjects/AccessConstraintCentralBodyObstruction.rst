AccessConstraintCentralBodyObstruction
======================================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Class defining constraints in terms of obstruction by a specified central body.

.. py:currentmodule:: AccessConstraintCentralBodyObstruction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.is_obstruction_assigned`
              - Check whether a central body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.add_obstruction`
              - Add a Central Body Obstruction by Name.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.remove_obstruction`
              - Remove a Central Body Obstruction by Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.assigned_obstructions`
              - Gets the Assigned Obstructions.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.available_obstructions`
              - Gets the Available Obstructions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintCentralBodyObstruction


Property detail
---------------

.. py:property:: assigned_obstructions
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.assigned_obstructions
    :type: list

    Gets the Assigned Obstructions.

.. py:property:: available_obstructions
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.available_obstructions
    :type: list

    Gets the Available Obstructions.


Method detail
-------------


.. py:method:: is_obstruction_assigned(self, obstruction: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.is_obstruction_assigned

    Check whether a central body is already assigned.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.add_obstruction

    Add a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction.remove_obstruction

    Remove a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`


