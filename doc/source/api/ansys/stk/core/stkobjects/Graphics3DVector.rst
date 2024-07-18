Graphics3DVector
================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DVector

   Bases: 

   Class defining 3D vectors.

.. py:currentmodule:: Graphics3DVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVector.reference_crdns`
              - Gets a collection that manages the 3D VGT visualizations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVector.vector_size_scale`
              - The size scale of the geometric elements. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVector.scale_relative_to_model`
              - Controls whether to scale the geometric elements relative to an object scale with the object's model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVector.angle_size_scale`
              - The angle size scale. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DVector


Property detail
---------------

.. py:property:: reference_crdns
    :canonical: ansys.stk.core.stkobjects.Graphics3DVector.reference_crdns
    :type: IGraphics3DReferenceAnalysisWorkbenchCollection

    Gets a collection that manages the 3D VGT visualizations.

.. py:property:: vector_size_scale
    :canonical: ansys.stk.core.stkobjects.Graphics3DVector.vector_size_scale
    :type: float

    The size scale of the geometric elements. Dimensionless.

.. py:property:: scale_relative_to_model
    :canonical: ansys.stk.core.stkobjects.Graphics3DVector.scale_relative_to_model
    :type: bool

    Controls whether to scale the geometric elements relative to an object scale with the object's model.

.. py:property:: angle_size_scale
    :canonical: ansys.stk.core.stkobjects.Graphics3DVector.angle_size_scale
    :type: float

    The angle size scale. Dimensionless.


