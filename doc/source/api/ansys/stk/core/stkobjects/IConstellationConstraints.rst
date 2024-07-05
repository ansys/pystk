IConstellationConstraints
=========================

.. py:class:: ansys.stk.core.stkobjects.IConstellationConstraints

   object
   
   Constellation Constraints.

.. py:currentmodule:: IConstellationConstraints

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.set_from_restriction_type`
              - Set a new restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.set_to_restriction_type`
              - Set a new restriction type when in the to access position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.from_parent_constraint`
              - Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'from' access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.to_parent_constraint`
              - Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'to' access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.from_restriction_type`
              - Gets the current restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.from_restriction`
              - Returns a restriction corresponding to the restriction type when in the from access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction_type`
              - Gets the current restriction type when in the to access position.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction`
              - Returns a restriction corresponding to the restriction type when in the to access position.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IConstellationConstraints


Property detail
---------------

.. py:property:: from_parent_constraint
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.from_parent_constraint
    :type: CONSTELLATION_FROM_TO_PARENT_CONSTRAINT

    Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'from' access position.

.. py:property:: to_parent_constraint
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.to_parent_constraint
    :type: CONSTELLATION_FROM_TO_PARENT_CONSTRAINT

    Constrain accesses for constellation objects when used in a chain by parent relationships when in the 'to' access position.

.. py:property:: from_restriction_type
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.from_restriction_type
    :type: CONSTELLATION_CONSTRAINT_RESTRICTION

    Gets the current restriction type when in the from access position.

.. py:property:: from_restriction
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.from_restriction
    :type: IConstellationConstraintRestriction

    Returns a restriction corresponding to the restriction type when in the from access position.

.. py:property:: to_restriction_type
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction_type
    :type: CONSTELLATION_CONSTRAINT_RESTRICTION

    Gets the current restriction type when in the to access position.

.. py:property:: to_restriction
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction
    :type: IConstellationConstraintRestriction

    Returns a restriction corresponding to the restriction type when in the to access position.


Method detail
-------------






.. py:method:: set_from_restriction_type(self, restriction: CONSTELLATION_CONSTRAINT_RESTRICTION) -> None
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.set_from_restriction_type

    Set a new restriction type when in the from access position.

    :Parameters:

    **restriction** : :obj:`~CONSTELLATION_CONSTRAINT_RESTRICTION`

    :Returns:

        :obj:`~None`



.. py:method:: set_to_restriction_type(self, restriction: CONSTELLATION_CONSTRAINT_RESTRICTION) -> None
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.set_to_restriction_type

    Set a new restriction type when in the to access position.

    :Parameters:

    **restriction** : :obj:`~CONSTELLATION_CONSTRAINT_RESTRICTION`

    :Returns:

        :obj:`~None`


