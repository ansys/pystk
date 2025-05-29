ConstellationConstraints
========================

.. py:class:: ansys.stk.core.stkobjects.ConstellationConstraints

   Class related to the constellation constraints.

.. py:currentmodule:: ConstellationConstraints

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.set_from_restriction_type`
              - Set a new restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.set_to_restriction_type`
              - Set a new restriction type when in the to access position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.from_parent_constraint`
              - Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'from' access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.to_parent_constraint`
              - Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'to' access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.from_restriction_type`
              - Get the current restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.from_restriction`
              - Return a restriction corresponding to the restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.to_restriction_type`
              - Get the current restriction type when in the to access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ConstellationConstraints.to_restriction`
              - Return a restriction corresponding to the restriction type when in the to access position.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ConstellationConstraints


Property detail
---------------

.. py:property:: from_parent_constraint
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.from_parent_constraint
    :type: ConstellationFromToParentConstraint

    Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'from' access position.

.. py:property:: to_parent_constraint
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.to_parent_constraint
    :type: ConstellationFromToParentConstraint

    Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'to' access position.

.. py:property:: from_restriction_type
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.from_restriction_type
    :type: ConstellationConstraintRestrictionType

    Get the current restriction type when in the from access position.

.. py:property:: from_restriction
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.from_restriction
    :type: IConstellationConstraintRestriction

    Return a restriction corresponding to the restriction type when in the from access position.

.. py:property:: to_restriction_type
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.to_restriction_type
    :type: ConstellationConstraintRestrictionType

    Get the current restriction type when in the to access position.

.. py:property:: to_restriction
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.to_restriction
    :type: IConstellationConstraintRestriction

    Return a restriction corresponding to the restriction type when in the to access position.


Method detail
-------------






.. py:method:: set_from_restriction_type(self, restriction: ConstellationConstraintRestrictionType) -> None
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.set_from_restriction_type

    Set a new restriction type when in the from access position.

    :Parameters:

        **restriction** : :obj:`~ConstellationConstraintRestrictionType`


    :Returns:

        :obj:`~None`



.. py:method:: set_to_restriction_type(self, restriction: ConstellationConstraintRestrictionType) -> None
    :canonical: ansys.stk.core.stkobjects.ConstellationConstraints.set_to_restriction_type

    Set a new restriction type when in the to access position.

    :Parameters:

        **restriction** : :obj:`~ConstellationConstraintRestrictionType`


    :Returns:

        :obj:`~None`


