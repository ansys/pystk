IVectorGeometryToolVectorModelAttach
====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorModelAttach

   object
   
   Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: IVectorGeometryToolVectorModelAttach

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorModelAttach.pointable_element_name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorModelAttach


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorModelAttach.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


