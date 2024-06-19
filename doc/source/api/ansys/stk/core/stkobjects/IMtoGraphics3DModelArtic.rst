IMtoGraphics3DModelArtic
========================

.. py:class:: IMtoGraphics3DModelArtic

   object
   
   MTO ModelArticulation Interface.

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
            * - :py:meth:`~read_artic_file_on_load`
            * - :py:meth:`~save_artic_file_on_save`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DModelArtic


Property detail
---------------

.. py:property:: enable_default_save
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.enable_default_save
    :type: bool

    Save the articulation value as the default for all future sessions using this model. The articulation value is saved with the object and not with the model or articulation files.

.. py:property:: lod_count
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.lod_count
    :type: int

    Specify the level of detail (LOD) for defining articulations, where 0 is the finest level of detail and 1 is the coarsest model.

.. py:property:: read_artic_file_on_load
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.read_artic_file_on_load
    :type: bool

    Read the articulation file when MTO object is loaded.

.. py:property:: save_artic_file_on_save
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.save_artic_file_on_save
    :type: bool

    Save the articulations to the articulation file when MTO object is saved.


Method detail
-------------



.. py:method:: get_transformation_value(self, lOD: int, articulation: str, trans: str) -> float
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.get_transformation_value

    Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`

    :Returns:

        :obj:`~float`

.. py:method:: set_transformation_value(self, lOD: int, articulation: str, trans: str, transVal: float) -> None
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.set_transformation_value

    Set the Transformation Value given the LOD and articulation name.

    :Parameters:

    **lOD** : :obj:`~int`
    **articulation** : :obj:`~str`
    **trans** : :obj:`~str`
    **transVal** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: get_available_articulations(self, lOD: int) -> list
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.get_available_articulations

    Get the available articulations.

    :Parameters:

    **lOD** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: get_available_transformations(self, lOD: int, articName: str) -> IGraphics3DModelTransformationCollection
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DModelArtic.get_available_transformations

    Get the available transformations.

    :Parameters:

    **lOD** : :obj:`~int`
    **articName** : :obj:`~str`

    :Returns:

        :obj:`~IGraphics3DModelTransformationCollection`






