IGraphics3DModelArtic
=====================

.. py:class:: IGraphics3DModelArtic

   object
   
   ModelArticulation Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_transformation_value`
              - Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.
            * - :py:meth:`~set_transformation_value`
              - Set the Transformation Value given the LOD and articulation name.
            * - :py:meth:`~get_available_articulations`
              - Get the available articulations.
            * - :py:meth:`~get_available_transformations`
              - Get the available transformations.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_default_save`
            * - :py:meth:`~lod_count`
            * - :py:meth:`~use_object_color_for_model`
            * - :py:meth:`~save_artic_file_on_save`
            * - :py:meth:`~use_articulation_file`
            * - :py:meth:`~graphics_3d_articulation_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModelArtic


Property detail
---------------

.. py:property:: enable_default_save
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.enable_default_save
    :type: bool

    Save the articulation value as the default for all future sessions using this model. The articulation value is saved with the object and not with the model or articulation files.

.. py:property:: lod_count
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.lod_count
    :type: int

    Specify the level of detail (LOD) for defining articulations, where 0 is the finest level of detail and 1 is the coarsest model.

.. py:property:: use_object_color_for_model
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.use_object_color_for_model
    :type: bool

    Set Model Color to facility color if color articulation exists.

.. py:property:: save_artic_file_on_save
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.save_artic_file_on_save
    :type: bool

    Save articulation file associated with the model when the object is saved.

.. py:property:: use_articulation_file
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.use_articulation_file
    :type: bool

    Use the articulation from the specified file.

.. py:property:: graphics_3d_articulation_file
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.graphics_3d_articulation_file
    :type: "IAgVOArticulationFile"

    Interface to specify articulation file.


Method detail
-------------



.. py:method:: get_transformation_value(self, lOD:int, articulation:str, trans:str) -> float

    Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`

    :Returns:

        :obj:`~float`

.. py:method:: set_transformation_value(self, lOD:int, articulation:str, trans:str, transVal:float) -> None

    Set the Transformation Value given the LOD and articulation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`
    **transVal** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: get_available_articulations(self, lOD:int) -> list

    Get the available articulations.

    :Parameters:

    **lOD** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: get_available_transformations(self, lOD:int, articName:str) -> "IGraphics3DModelTransformationCollection"

    Get the available transformations.

    :Parameters:

    **lOD** : :obj:`~int`
    **articName** : :obj:`~str`

    :Returns:

        :obj:`~"IGraphics3DModelTransformationCollection"`









