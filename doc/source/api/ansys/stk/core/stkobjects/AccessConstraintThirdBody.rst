AccessConstraintThirdBody
=========================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintThirdBody

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Do not use this class, as it is deprecated. Use AccessConstraintCentralBodyObstruction instead. Class defining Central Body Obstruction constraints.

.. py:currentmodule:: AccessConstraintThirdBody

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody.is_obstruction_assigned`
              - Do not use this method, as it is deprecated. Use IsObstructionAssigned on AccessConstraintCentralBodyObstruction instead. Check whether a third body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody.add_obstruction`
              - Do not use this method, as it is deprecated. Use AddObstruction on AccessConstraintCentralBodyObstruction instead. Adds an Obstruction by Name.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody.remove_obstruction`
              - Do not use this method, as it is deprecated. Use RemoveObstruction on AccessConstraintCentralBodyObstruction instead. Remove an Obstruction by Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody.assigned_obstructions`
              - Do not use this property, as it is deprecated. Use AssignedObstructions on AccessConstraintCentralBodyObstruction instead. Gets the Assigned Obstructions.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody.available_obstructions`
              - Do not use this property, as it is deprecated. Use AvailableObstructions on AccessConstraintCentralBodyObstruction instead. Gets the Available Obstructions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintThirdBody


Property detail
---------------

.. py:property:: assigned_obstructions
    :canonical: ansys.stk.core.stkobjects.AccessConstraintThirdBody.assigned_obstructions
    :type: list

    Do not use this property, as it is deprecated. Use AssignedObstructions on AccessConstraintCentralBodyObstruction instead. Gets the Assigned Obstructions.

.. py:property:: available_obstructions
    :canonical: ansys.stk.core.stkobjects.AccessConstraintThirdBody.available_obstructions
    :type: list

    Do not use this property, as it is deprecated. Use AvailableObstructions on AccessConstraintCentralBodyObstruction instead. Gets the Available Obstructions.


Method detail
-------------


.. py:method:: is_obstruction_assigned(self, obstruction: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintThirdBody.is_obstruction_assigned

    Do not use this method, as it is deprecated. Use IsObstructionAssigned on AccessConstraintCentralBodyObstruction instead. Check whether a third body is already assigned.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintThirdBody.add_obstruction

    Do not use this method, as it is deprecated. Use AddObstruction on AccessConstraintCentralBodyObstruction instead. Adds an Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintThirdBody.remove_obstruction

    Do not use this method, as it is deprecated. Use RemoveObstruction on AccessConstraintCentralBodyObstruction instead. Remove an Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`


