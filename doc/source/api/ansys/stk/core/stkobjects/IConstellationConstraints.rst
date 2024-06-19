IConstellationConstraints
=========================

.. py:class:: IConstellationConstraints

   object
   
   Constellation Constraints.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_from_restriction_type`
              - Set a new restriction type when in the from access position.
            * - :py:meth:`~set_to_restriction_type`
              - Set a new restriction type when in the to access position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~from_parent_constraint`
            * - :py:meth:`~to_parent_constraint`
            * - :py:meth:`~from_restriction_type`
            * - :py:meth:`~from_restriction`
            * - :py:meth:`~to_restriction_type`
            * - :py:meth:`~to_restriction`


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
    :type: IAgCnCnstrRestriction

    Returns a restriction corresponding to the restriction type when in the from access position.

.. py:property:: to_restriction_type
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction_type
    :type: CONSTELLATION_CONSTRAINT_RESTRICTION

    Gets the current restriction type when in the to access position.

.. py:property:: to_restriction
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraints.to_restriction
    :type: IAgCnCnstrRestriction

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


