IVectorGeometryToolPointGlint
=============================

.. py:class:: IVectorGeometryToolPointGlint

   object
   
   Point on central body surface that reflects from source to observer.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~source_point`
            * - :py:meth:`~observer_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointGlint


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.central_body
    :type: IAgCrdnCentralBodyRefTo

    Specify a central body.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.source_point
    :type: IAgCrdnPointRefTo

    Specify a source point.

.. py:property:: observer_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.observer_point
    :type: IAgCrdnPointRefTo

    Specify an observer point.


