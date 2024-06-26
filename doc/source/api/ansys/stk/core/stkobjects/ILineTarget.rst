ILineTarget
===========

.. py:class:: ansys.stk.core.stkobjects.ILineTarget

   object
   
   Line Target Path properties.

.. py:currentmodule:: ILineTarget

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTarget.points`
              - Get the points table, which displays a summary of the latitude and longitude values for each point, and indicates which point is currently defined as the anchor point.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTarget.graphics`
              - Returns the 2D graphics properties of the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTarget.graphics_3d`
              - Returns the 3D graphics properties of the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTarget.access_constraints`
              - Returns the constraints for the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTarget.allow_object_access`
              - Opt to have access to the object constrained to when it applies to the entire object,rather than any part of it.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILineTarget


Property detail
---------------

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.ILineTarget.points
    :type: ILineTargetPointCollection

    Get the points table, which displays a summary of the latitude and longitude values for each point, and indicates which point is currently defined as the anchor point.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ILineTarget.graphics
    :type: ILineTargetGraphics

    Returns the 2D graphics properties of the line target.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ILineTarget.graphics_3d
    :type: ILineTargetGraphics3D

    Returns the 3D graphics properties of the line target.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.ILineTarget.access_constraints
    :type: IAccessConstraintCollection

    Returns the constraints for the line target.

.. py:property:: allow_object_access
    :canonical: ansys.stk.core.stkobjects.ILineTarget.allow_object_access
    :type: bool

    Opt to have access to the object constrained to when it applies to the entire object,rather than any part of it.


