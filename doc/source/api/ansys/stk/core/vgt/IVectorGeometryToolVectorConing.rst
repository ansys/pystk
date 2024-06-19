IVectorGeometryToolVectorConing
===============================

.. py:class:: IVectorGeometryToolVectorConing

   object
   
   Vector created by revolving the Reference vector around the About vector with the specified rate.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~about_vector`
            * - :py:meth:`~reference_vector`
            * - :py:meth:`~start_clock_angle`
            * - :py:meth:`~stop_clock_angle`
            * - :py:meth:`~start_epoch`
            * - :py:meth:`~clock_angle_rate`
            * - :py:meth:`~mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorConing


Property detail
---------------

.. py:property:: about_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.about_vector
    :type: IAgCrdnVectorRefTo

    Specify a vector around which the the reference vector is revolved.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.reference_vector
    :type: IAgCrdnVectorRefTo

    Specify a reference vector.

.. py:property:: start_clock_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.start_clock_angle
    :type: float

    Specify a start angle.

.. py:property:: stop_clock_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.stop_clock_angle
    :type: float

    Specify a stop angle.

.. py:property:: start_epoch
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.start_epoch
    :type: typing.Any

    Specify an epoch at which the coning vector is aligned with the reference vector.

.. py:property:: clock_angle_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.clock_angle_rate
    :type: float

    Specify a rotation rate.

.. py:property:: mode
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorConing.mode
    :type: CRDN_SWEEP_MODE

    Specify either unidirectional or bidirectional mode.


