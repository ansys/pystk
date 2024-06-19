IVectorGeometryToolVectorApoapsis
=================================

.. py:class:: IVectorGeometryToolVectorApoapsis

   object
   
   Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_point`
            * - :py:meth:`~central_body`
            * - :py:meth:`~mean_element_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorApoapsis


Property detail
---------------

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorApoapsis.reference_point
    :type: IAgCrdnPointRefTo

    Specify a reference point.

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorApoapsis.central_body
    :type: IAgCrdnCentralBodyRefTo

    Specify a central body.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorApoapsis.mean_element_type
    :type: CRDN_MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


