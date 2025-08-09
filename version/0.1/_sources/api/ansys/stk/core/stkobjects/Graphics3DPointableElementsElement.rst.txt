Graphics3DPointableElementsElement
==================================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DPointableElementsElement

   Pointable elements for 3D model pointing.

.. py:currentmodule:: Graphics3DPointableElementsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.pointing_name`
              - Name of a movable element associated with a pointing parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.assigned_target_object`
              - Get the assigned target for the pointable element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.intervals`
              - Get a collection of intervals during which an 3d model part points towards selected targets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DPointableElementsElement


Property detail
---------------

.. py:property:: pointing_name
    :canonical: ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.pointing_name
    :type: str

    Name of a movable element associated with a pointing parameter.

.. py:property:: assigned_target_object
    :canonical: ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.assigned_target_object
    :type: LinkToObject

    Get the assigned target for the pointable element.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.Graphics3DPointableElementsElement.intervals
    :type: TimeIntervalCollection

    Get a collection of intervals during which an 3d model part points towards selected targets.


