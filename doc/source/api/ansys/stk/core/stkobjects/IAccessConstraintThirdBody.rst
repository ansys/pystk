IAccessConstraintThirdBody
==========================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraintThirdBody

   IAccessConstraint
   
   Do not use this interface, as it is deprecated. Use IAgAccessCnstrCbObstruction instead. Access Constraint Used for Third Body Obstructions.

.. py:currentmodule:: IAccessConstraintThirdBody

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintThirdBody.is_obstruction_assigned`
              - Do not use this method, as it is deprecated. Use IsObstructionAssigned on IAgAccessCnstrCbObstruction instead. Check whether a third body is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintThirdBody.add_obstruction`
              - Do not use this method, as it is deprecated. Use AddObstruction on IAgAccessCnstrCbObstruction instead. Adds an Obstruction by Name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintThirdBody.remove_obstruction`
              - Do not use this method, as it is deprecated. Use RemoveObstruction on IAgAccessCnstrCbObstruction instead. Remove an Obstruction by Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintThirdBody.assigned_obstructions`
              - This property is deprecated. Use AssignedObstructions on IAgAccessCnstrCbObstruction instead. Gets the Assigned Obstructions.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintThirdBody.available_obstructions`
              - This property is deprecated. Use AvailableObstructions on IAgAccessCnstrCbObstruction instead. Gets the Available Obstructions.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintThirdBody


Property detail
---------------

.. py:property:: assigned_obstructions
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintThirdBody.assigned_obstructions
    :type: list

    This property is deprecated. Use AssignedObstructions on IAgAccessCnstrCbObstruction instead. Gets the Assigned Obstructions.

.. py:property:: available_obstructions
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintThirdBody.available_obstructions
    :type: list

    This property is deprecated. Use AvailableObstructions on IAgAccessCnstrCbObstruction instead. Gets the Available Obstructions.


Method detail
-------------


.. py:method:: is_obstruction_assigned(self, obstruction: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintThirdBody.is_obstruction_assigned

    Do not use this method, as it is deprecated. Use IsObstructionAssigned on IAgAccessCnstrCbObstruction instead. Check whether a third body is already assigned.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintThirdBody.add_obstruction

    Do not use this method, as it is deprecated. Use AddObstruction on IAgAccessCnstrCbObstruction instead. Adds an Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_obstruction(self, obstruction: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintThirdBody.remove_obstruction

    Do not use this method, as it is deprecated. Use RemoveObstruction on IAgAccessCnstrCbObstruction instead. Remove an Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`


