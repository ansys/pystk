IGraphics3DModel
================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DModel

   object
   
   AgVOModel used to access the 3D model attributes.

.. py:currentmodule:: IGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.visible`
              - Display one or several models in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.scale_value`
              - Specify the absolute scaling value for the object. The model scale is an exponential scale. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.detail_threshold`
              - Gets the detail threshold attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.model_data`
              - Gets the model data property.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.model_type`
              - Gets or sets the model type property. A member of the AgEModelType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModel.articulation`
              - Articulation property.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModel


Property detail
---------------

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.visible
    :type: bool

    Display one or several models in the 3D Graphics window.

.. py:property:: scale_value
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.scale_value
    :type: float

    Specify the absolute scaling value for the object. The model scale is an exponential scale. Dimensionless.

.. py:property:: detail_threshold
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.detail_threshold
    :type: IGraphics3DDetailThreshold

    Gets the detail threshold attributes.

.. py:property:: model_data
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.model_data
    :type: IGraphics3DModelData

    Gets the model data property.

.. py:property:: model_type
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.model_type
    :type: MODEL_TYPE

    Gets or sets the model type property. A member of the AgEModelType enumeration.

.. py:property:: articulation
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.articulation
    :type: IGraphics3DModelArtic

    Articulation property.


