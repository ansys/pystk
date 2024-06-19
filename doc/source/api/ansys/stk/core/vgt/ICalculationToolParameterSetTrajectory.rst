ICalculationToolParameterSetTrajectory
======================================

.. py:class:: ICalculationToolParameterSetTrajectory

   object
   
   Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point`
            * - :py:meth:`~reference_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetTrajectory.point
    :type: IAgCrdnPoint

    Get the point for which trajectory representations are computed.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetTrajectory.reference_system
    :type: IAgCrdnSystem

    Get the reference system relative to which trajectory representations are computed.


