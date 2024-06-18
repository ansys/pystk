IAccessConstraintCentralBodyObstruction
=======================================

.. py:class:: IAccessConstraintCentralBodyObstruction

   IAccessConstraint
   
   Access Constraint used for Central Body Obstruction.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_obstruction_assigned`
              - Check whether a central body is already assigned.
            * - :py:meth:`~add_obstruction`
              - Add a Central Body Obstruction by Name.
            * - :py:meth:`~remove_obstruction`
              - Remove a Central Body Obstruction by Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~assigned_obstructions`
            * - :py:meth:`~available_obstructions`


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


.. py:method:: is_obstruction_assigned(self, obstruction:str) -> bool

    Check whether a central body is already assigned.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_obstruction(self, obstruction:str) -> None

    Add a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_obstruction(self, obstruction:str) -> None

    Remove a Central Body Obstruction by Name.

    :Parameters:

    **obstruction** : :obj:`~str`

    :Returns:

        :obj:`~None`


