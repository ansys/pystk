IEOIRShape
==========

.. py:class:: IEOIRShape

   object
   
   A shape interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~shape_type`
            * - :py:meth:`~mesh_file`
            * - :py:meth:`~shape_object`
            * - :py:meth:`~dimension_a`
            * - :py:meth:`~dimension_b`
            * - :py:meth:`~dimension_c`
            * - :py:meth:`~material_specification_type`
            * - :py:meth:`~material_map_file`
            * - :py:meth:`~material_element_index`
            * - :py:meth:`~material_elements_count`
            * - :py:meth:`~material_elements`
            * - :py:meth:`~target_signature_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IEOIRShape


Property detail
---------------

.. py:property:: shape_type
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.shape_type
    :type: EOIR_SHAPE_TYPE

    Property used to access the shape type.

.. py:property:: mesh_file
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.mesh_file
    :type: str

    Property used to access the mesh file.

.. py:property:: shape_object
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.shape_object
    :type: IAgEOIRShapeObject

    Property used to access the shape object.

.. py:property:: dimension_a
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.dimension_a
    :type: float

    Property used to access the A dimension.

.. py:property:: dimension_b
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.dimension_b
    :type: float

    Property used to access the B dimension.

.. py:property:: dimension_c
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.dimension_c
    :type: float

    Property used to access the C dimension.

.. py:property:: material_specification_type
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.material_specification_type
    :type: EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE

    Property used to access the shape material specification type.

.. py:property:: material_map_file
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.material_map_file
    :type: str

    Property used to access the material map file.

.. py:property:: material_element_index
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.material_element_index
    :type: int

    Property used to access the currently selected material element index.

.. py:property:: material_elements_count
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.material_elements_count
    :type: int

    Property used to access the number of material elements.

.. py:property:: material_elements
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.material_elements
    :type: IAgEOIRMaterialElementCollection

    Property used to access the material element collection.

.. py:property:: target_signature_file
    :canonical: ansys.stk.core.stkobjects.IEOIRShape.target_signature_file
    :type: str

    Property used to access the target signature file.


