AccessConstraintObjExAngle
==========================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintObjExAngle

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Class defining the Object Exclusion Angle constraint.

.. py:currentmodule:: AccessConstraintObjExAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.add_exclusion_object`
              - Add an exclusion object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.is_object_assigned`
              - Return true if an exclusion object is assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.remove_exclusion_object`
              - Remove an exclusion object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.exclusion_angle`
              - Exclusion Angle value. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.assigned_objects`
              - Returns a safearray of assigned objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle.available_objects`
              - Returns a safearray of available objects.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintObjExAngle


Property detail
---------------

.. py:property:: exclusion_angle
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.exclusion_angle
    :type: typing.Any

    Exclusion Angle value. Uses Angle Dimension.

.. py:property:: assigned_objects
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.assigned_objects
    :type: list

    Returns a safearray of assigned objects.

.. py:property:: available_objects
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.available_objects
    :type: list

    Returns a safearray of available objects.


Method detail
-------------





.. py:method:: add_exclusion_object(self, object_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.add_exclusion_object

    Add an exclusion object.

    :Parameters:

    **object_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: is_object_assigned(self, object_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.is_object_assigned

    Return true if an exclusion object is assigned.

    :Parameters:

    **object_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_exclusion_object(self, object_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintObjExAngle.remove_exclusion_object

    Remove an exclusion object.

    :Parameters:

    **object_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

