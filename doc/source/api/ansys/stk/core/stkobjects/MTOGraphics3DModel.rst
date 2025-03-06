MTOGraphics3DModel
==================

.. py:class:: ansys.stk.core.stkobjects.MTOGraphics3DModel

   MTO track model options.

.. py:currentmodule:: MTOGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.show_graphics`
              - Opt whether to use a model to represent the track in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.filename`
              - Get or set the name of the track model file.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.scale_value`
              - Get or set the exponential scaling value for the track model.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.initial_bearing`
              - Get or set the initial bearing of the model, relative to north. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.z_points_nadir`
              - Opt whether to have the Z axis point to nadir (to orient it as an aircraft) or not (to orient it as a surface vehicle).
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.articulation`
              - Configures the model articulations.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DModel.file_path`
              - Get the full path and file name of the track model file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGraphics3DModel


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.show_graphics
    :type: bool

    Opt whether to use a model to represent the track in the 3D Graphics window.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.filename
    :type: str

    Get or set the name of the track model file.

.. py:property:: scale_value
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.scale_value
    :type: float

    Get or set the exponential scaling value for the track model.

.. py:property:: initial_bearing
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.initial_bearing
    :type: float

    Get or set the initial bearing of the model, relative to north. Uses Angle Dimension.

.. py:property:: z_points_nadir
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.z_points_nadir
    :type: bool

    Opt whether to have the Z axis point to nadir (to orient it as an aircraft) or not (to orient it as a surface vehicle).

.. py:property:: articulation
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.articulation
    :type: MTOGraphics3DModelArticulation

    Configures the model articulations.

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DModel.file_path
    :type: str

    Get the full path and file name of the track model file.


