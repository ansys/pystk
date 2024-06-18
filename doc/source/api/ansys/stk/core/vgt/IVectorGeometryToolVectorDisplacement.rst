IVectorGeometryToolVectorDisplacement
=====================================

.. py:class:: IVectorGeometryToolVectorDisplacement

   object
   
   Vector defined by its start and end points.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~origin`
            * - :py:meth:`~destination`
            * - :py:meth:`~apparent`
            * - :py:meth:`~ignore_aberration`
            * - :py:meth:`~signal_sense`
            * - :py:meth:`~reference_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorDisplacement


Property detail
---------------

.. py:property:: origin
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.origin
    :type: "IAgCrdnPointRefTo"

    Specify the vector's origin point.

.. py:property:: destination
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.destination
    :type: "IAgCrdnPointRefTo"

    Specify the vector's destination point.

.. py:property:: apparent
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.apparent
    :type: bool

    Controls whether to take a light speed delay into account.

.. py:property:: ignore_aberration
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.ignore_aberration
    :type: bool

    Set to true if you do not want to calculate the aberration correction. This property is read-only if Apparent is set to false.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.signal_sense
    :type: "CRDN_SIGNAL_SENSE"

    Specify a sense of signal transmission. This property is read-only if Apparent is set to false.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDisplacement.reference_system
    :type: "IAgCrdnSystemRefTo"

    Specify a frame in which the light time delay is computed. This property is read-only if Apparent is set to false.


