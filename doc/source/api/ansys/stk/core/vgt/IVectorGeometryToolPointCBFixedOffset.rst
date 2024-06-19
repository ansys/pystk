IVectorGeometryToolPointCBFixedOffset
=====================================

.. py:class:: IVectorGeometryToolPointCBFixedOffset

   object
   
   Point specified by fixed components with respect to central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~reference_shape`
            * - :py:meth:`~position`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointCBFixedOffset


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCBFixedOffset.central_body
    :type: str

    Get the central body.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCBFixedOffset.reference_shape
    :type: CRDN_REFERENCE_SHAPE_TYPE

    Choose the point height's reference. Available options are central body ellipsoid (WSG84), terrain or Mean Sea Level.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCBFixedOffset.position
    :type: IAgPosition

    A position of the point fixed on the central body.


