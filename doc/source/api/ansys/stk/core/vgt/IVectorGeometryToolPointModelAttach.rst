IVectorGeometryToolPointModelAttach
===================================

.. py:class:: IVectorGeometryToolPointModelAttach

   object
   
   A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pointable_element_name`
            * - :py:meth:`~use_scale`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointModelAttach


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointModelAttach.pointable_element_name
    :type: str

    Specify a model attachment point.

.. py:property:: use_scale
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointModelAttach.use_scale
    :type: bool

    Specify whether to use the model scale.


