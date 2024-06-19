ILineTarget
===========

.. py:class:: ILineTarget

   object
   
   Line Target Path properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~points`
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~allow_object_access`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILineTarget


Property detail
---------------

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.ILineTarget.points
    :type: IAgLtPointCollection

    Get the points table, which displays a summary of the latitude and longitude values for each point, and indicates which point is currently defined as the anchor point.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ILineTarget.graphics
    :type: IAgLtGraphics

    Returns the 2D graphics properties of the line target.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ILineTarget.graphics_3d
    :type: IAgLtVO

    Returns the 3D graphics properties of the line target.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.ILineTarget.access_constraints
    :type: IAgAccessConstraintCollection

    Returns the constraints for the line target.

.. py:property:: allow_object_access
    :canonical: ansys.stk.core.stkobjects.ILineTarget.allow_object_access
    :type: bool

    Opt to have access to the object constrained to when it applies to the entire object,rather than any part of it.


