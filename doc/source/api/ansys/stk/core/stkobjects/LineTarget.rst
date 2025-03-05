LineTarget
==========

.. py:class:: ansys.stk.core.stkobjects.LineTarget

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Line Target Path properties.

.. py:currentmodule:: LineTarget

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LineTarget.points`
              - Get the points table, which displays a summary of the latitude and longitude values for each point, and indicates which point is currently defined as the anchor point.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTarget.graphics`
              - Return the 2D graphics properties of the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTarget.graphics_3d`
              - Return the 3D graphics properties of the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTarget.access_constraints`
              - Return the constraints for the line target.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTarget.allow_object_access`
              - Opt to have access to the object constrained to when it applies to the entire object,rather than any part of it.



Examples
--------

Create a New Line Target (on the current scenario central body)

.. code-block:: python

    # Scenario scenario: Scenario object
    lineTarget = scenario.children.new(STKObjectType.LINE_TARGET, "MyLineTarget")
    point1 = lineTarget.points.add(34.72, -118.34)
    point2 = lineTarget.points.add(30.83, -82.67)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LineTarget


Property detail
---------------

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.LineTarget.points
    :type: LineTargetPointCollection

    Get the points table, which displays a summary of the latitude and longitude values for each point, and indicates which point is currently defined as the anchor point.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.LineTarget.graphics
    :type: LineTargetGraphics

    Return the 2D graphics properties of the line target.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.LineTarget.graphics_3d
    :type: LineTargetGraphics3D

    Return the 3D graphics properties of the line target.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.LineTarget.access_constraints
    :type: AccessConstraintCollection

    Return the constraints for the line target.

.. py:property:: allow_object_access
    :canonical: ansys.stk.core.stkobjects.LineTarget.allow_object_access
    :type: bool

    Opt to have access to the object constrained to when it applies to the entire object,rather than any part of it.


