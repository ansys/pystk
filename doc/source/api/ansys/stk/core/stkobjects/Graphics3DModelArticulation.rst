Graphics3DModelArticulation
===========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DModelArticulation

   Class defining 3D model articulations.

.. py:currentmodule:: Graphics3DModelArticulation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_available_articulations`
              - Get the available articulations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_available_transformations`
              - Get the available transformations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_transformation_value`
              - Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.set_transformation_value`
              - Set the Transformation Value given the LOD and articulation name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.enable_default_save`
              - Save the articulation value as the default for all future sessions using this model. The articulation value is saved with the object and not with the model or articulation files.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.graphics_3d_articulation_file`
              - Interface to specify articulation file.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.level_of_detail_count`
              - Specify the level of detail (LOD) for defining articulations, where 0 is the finest level of detail and 1 is the coarsest model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.save_articulation_file_on_save`
              - Save articulation file associated with the model when the object is saved.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.use_articulation_file`
              - Use the articulation from the specified file.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation.use_object_color_for_model`
              - Set Model Color to facility color if color articulation exists.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DModelArticulation


Property detail
---------------

.. py:property:: enable_default_save
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.enable_default_save
    :type: bool

    Save the articulation value as the default for all future sessions using this model. The articulation value is saved with the object and not with the model or articulation files.

.. py:property:: graphics_3d_articulation_file
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.graphics_3d_articulation_file
    :type: Graphics3DArticulationFile

    Interface to specify articulation file.

.. py:property:: level_of_detail_count
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.level_of_detail_count
    :type: int

    Specify the level of detail (LOD) for defining articulations, where 0 is the finest level of detail and 1 is the coarsest model.

.. py:property:: save_articulation_file_on_save
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.save_articulation_file_on_save
    :type: bool

    Save articulation file associated with the model when the object is saved.

.. py:property:: use_articulation_file
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.use_articulation_file
    :type: bool

    Use the articulation from the specified file.

.. py:property:: use_object_color_for_model
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.use_object_color_for_model
    :type: bool

    Set Model Color to facility color if color articulation exists.


Method detail
-------------



.. py:method:: get_available_articulations(self, level_of_detail: int) -> list
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_available_articulations

    Get the available articulations.

    :Parameters:

        **level_of_detail** : :obj:`~int`


    :Returns:

        :obj:`~list`

.. py:method:: get_available_transformations(self, level_of_detail: int, artic_name: str) -> Graphics3DModelTransformationCollection
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_available_transformations

    Get the available transformations.

    :Parameters:

        **level_of_detail** : :obj:`~int`

        **artic_name** : :obj:`~str`


    :Returns:

        :obj:`~Graphics3DModelTransformationCollection`

.. py:method:: get_transformation_value(self, level_of_detail: int, articulation: str, trans: str) -> float
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.get_transformation_value

    Get the Transformation Value given the LOD (level of detail), articulation name and the transformation name.

    :Parameters:

        **level_of_detail** : :obj:`~int`

        **articulation** : :obj:`~str`

        **trans** : :obj:`~str`


    :Returns:

        :obj:`~float`




.. py:method:: set_transformation_value(self, level_of_detail: int, articulation: str, trans: str, transformation_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelArticulation.set_transformation_value

    Set the Transformation Value given the LOD and articulation name.

    :Parameters:

        **level_of_detail** : :obj:`~int`

        **articulation** : :obj:`~str`

        **trans** : :obj:`~str`

        **transformation_value** : :obj:`~float`


    :Returns:

        :obj:`~None`






