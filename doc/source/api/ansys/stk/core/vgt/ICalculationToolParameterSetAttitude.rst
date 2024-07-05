ICalculationToolParameterSetAttitude
====================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolParameterSetAttitude

   object
   
   Attitude parameter set contains various representations of attitude of one set of axes relative to another.

.. py:currentmodule:: ICalculationToolParameterSetAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.axes`
              - Get the axes for which attitude representations are computed.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.reference_axes`
              - Get the reference axes relative to which attitude representations are computed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetAttitude


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.axes
    :type: IVectorGeometryToolAxes

    Get the axes for which attitude representations are computed.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.reference_axes
    :type: IVectorGeometryToolAxes

    Get the reference axes relative to which attitude representations are computed.


