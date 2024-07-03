IAccessConstraintObjExAngle
===========================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle

   IAccessConstraint
   
   Access Constraint used for Object Exclusion Angles.

.. py:currentmodule:: IAccessConstraintObjExAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.add_exclusion_object`
              - Add an exclusion object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.is_object_assigned`
              - Return true if an exclusion object is assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.remove_exclusion_object`
              - Remove an exclusion object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.exclusion_angle`
              - Exclusion Angle value. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.assigned_objects`
              - Returns a safearray of assigned objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.available_objects`
              - Returns a safearray of available objects.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintObjExAngle


Property detail
---------------

.. py:property:: exclusion_angle
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.exclusion_angle
    :type: typing.Any

    Exclusion Angle value. Uses Angle Dimension.

.. py:property:: assigned_objects
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.assigned_objects
    :type: list

    Returns a safearray of assigned objects.

.. py:property:: available_objects
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.available_objects
    :type: list

    Returns a safearray of available objects.


Method detail
-------------





.. py:method:: add_exclusion_object(self, objectName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.add_exclusion_object

    Add an exclusion object.

    :Parameters:

    **objectName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: is_object_assigned(self, objectName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.is_object_assigned

    Return true if an exclusion object is assigned.

    :Parameters:

    **objectName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_exclusion_object(self, objectName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintObjExAngle.remove_exclusion_object

    Remove an exclusion object.

    :Parameters:

    **objectName** : :obj:`~str`

    :Returns:

        :obj:`~None`

