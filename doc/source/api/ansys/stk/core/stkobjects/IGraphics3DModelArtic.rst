IGraphics3DModelArtic
=====================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DModelArtic

   object
   
   ModelArticulation Interface.

.. py:currentmodule:: IGraphics3DModelArtic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_transformation_value`
              - Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.set_transformation_value`
              - Set the Transformation Value given the LOD and articulation name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_available_articulations`
              - Get the available articulations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_available_transformations`
              - Get the available transformations.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.enable_default_save`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.lod_count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.use_object_color_for_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.save_artic_file_on_save`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.use_articulation_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelArtic.graphics_3d_articulation_file`


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
    :type: IGraphics3DArticulationFile

    Interface to specify articulation file.


Method detail
-------------



.. py:method:: get_transformation_value(self, lOD: int, articulation: str, trans: str) -> float
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_transformation_value

    Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`

    :Returns:

        :obj:`~float`

.. py:method:: set_transformation_value(self, lOD: int, articulation: str, trans: str, transVal: float) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.set_transformation_value

    Set the Transformation Value given the LOD and articulation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`
    **transVal** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: get_available_articulations(self, lOD: int) -> list
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_available_articulations

    Get the available articulations.

    :Parameters:

    **lOD** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: get_available_transformations(self, lOD: int, articName: str) -> IGraphics3DModelTransformationCollection
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelArtic.get_available_transformations

    Get the available transformations.

    :Parameters:

    **lOD** : :obj:`~int`
    **articName** : :obj:`~str`

    :Returns:

        :obj:`~IGraphics3DModelTransformationCollection`









