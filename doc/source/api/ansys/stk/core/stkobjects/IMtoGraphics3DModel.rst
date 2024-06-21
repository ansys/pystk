IMtoGraphics3DModel
===================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics3DModel

   object
   
   Interface for MTO track model options.

.. py:currentmodule:: IMtoGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.scale_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.initial_bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.z_points_nadir`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.articulation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DModel.file_path`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DModel


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.is_visible
    :type: bool

    Opt whether to use a model to represent the track in the 3D Graphics window.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.filename
    :type: str

    Gets or sets the name of the track model file.

.. py:property:: scale_value
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.scale_value
    :type: float

    Gets or sets the exponential scaling value for the track model.

.. py:property:: initial_bearing
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.initial_bearing
    :type: float

    Gets or sets the initial bearing of the model, relative to north. Uses Angle Dimension.

.. py:property:: z_points_nadir
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.z_points_nadir
    :type: bool

    Opt whether to have the Z axis point to nadir (to orient it as an aircraft) or not (to orient it as a surface vehicle).

.. py:property:: articulation
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.articulation
    :type: IMtoGraphics3DModelArtic

    Configures the model articulations.

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModel.file_path
    :type: str

    Get the full path and file name of the track model file.


