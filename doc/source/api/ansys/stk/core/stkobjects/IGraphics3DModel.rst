IGraphics3DModel
================

.. py:class:: IGraphics3DModel

   object
   
   AgVOModel used to access the 3D model attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~visible`
            * - :py:meth:`~scale_value`
            * - :py:meth:`~detail_threshold`
            * - :py:meth:`~model_data`
            * - :py:meth:`~model_type`
            * - :py:meth:`~articulation`


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
    :type: "IAgVODetailThreshold"

    Gets the detail threshold attributes.

.. py:property:: model_data
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.model_data
    :type: "IAgVOModelData"

    Gets the model data property.

.. py:property:: model_type
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.model_type
    :type: "MODEL_TYPE"

    Gets or sets the model type property. A member of the AgEModelType enumeration.

.. py:property:: articulation
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModel.articulation
    :type: "IAgVOModelArtic"

    Articulation property.


