IGraphics3DPointableElementsElement
===================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement

   object
   
   Pointable elements interface for 3D model pointing.

.. py:currentmodule:: IGraphics3DPointableElementsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.pointing_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.assigned_target_object`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DPointableElementsElement


Property detail
---------------

.. py:property:: pointing_name
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.pointing_name
    :type: str

    Name of a movable element associated with a pointing parameter.

.. py:property:: assigned_target_object
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.assigned_target_object
    :type: ILinkToObject

    Get the assigned target for the pointable element.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsElement.intervals
    :type: IIntervalCollection

    Gets a collection of intervals during which an 3d model part points towards selected targets.


