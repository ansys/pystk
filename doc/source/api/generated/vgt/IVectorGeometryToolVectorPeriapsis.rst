IVectorGeometryToolVectorPeriapsis
==================================

.. py:class:: IVectorGeometryToolVectorPeriapsis

   object
   
   Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~reference_point`
            * - :py:meth:`~mean_element_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorPeriapsis


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.central_body
    :type: "IAgCrdnCentralBodyRefTo"

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.reference_point
    :type: "IAgCrdnPointRefTo"

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.mean_element_type
    :type: "CRDN_MEAN_ELEMENT_THEORY"

    Specify the mean element theory type for approximating motion.


