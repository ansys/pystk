IMtoGraphics3DSwapDistances
===========================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances

   object
   
   Interface for MTO track 3D swap distances.

.. py:currentmodule:: IMtoGraphics3DSwapDistances

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.use_swap_distances`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.label_from`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.label_to`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.model_from`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.model_to`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.marker_from`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.marker_to`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.point_from`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.point_to`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DSwapDistances


Property detail
---------------

.. py:property:: use_swap_distances
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.use_swap_distances
    :type: bool

    Opt whether to set swap distances.

.. py:property:: label_from
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.label_from
    :type: float

    Specify the minimum distance from the viewer reference point at which the track label is visible. Uses Distance Dimension.

.. py:property:: label_to
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.label_to
    :type: float

    Specify the maximum distance from the viewer reference point at which the track label is visible. Uses Distance Dimension.

.. py:property:: model_from
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.model_from
    :type: float

    Specify the minimum distance from the viewer reference point at which the track model is visible. Uses Distance Dimension.

.. py:property:: model_to
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.model_to
    :type: float

    Specify the maximum distance from the viewer reference point at which the track model is visible. Uses Distance Dimension.

.. py:property:: marker_from
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.marker_from
    :type: float

    Specify the minimum distance from the viewer reference point at which the track marker is visible. Uses Distance Dimension.

.. py:property:: marker_to
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.marker_to
    :type: float

    Specify the maximum distance from the viewer reference point at which the track marker is visible. Uses Distance Dimension.

.. py:property:: point_from
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.point_from
    :type: float

    Specify the minimum distance from the viewer reference point at which the track point is visible. Uses Distance Dimension.

.. py:property:: point_to
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DSwapDistances.point_to
    :type: float

    Specify the maximum distance from the viewer reference point at which the track point is visible. Uses Distance Dimension.


