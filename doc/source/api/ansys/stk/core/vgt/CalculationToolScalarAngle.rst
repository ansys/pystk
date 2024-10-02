CalculationToolScalarAngle
==========================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarAngle

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Scalar equal to angular displacement obtained from any angle in VGT.

.. py:currentmodule:: CalculationToolScalarAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarAngle.input_angle`
              - The input angle, which is a VGT angle component. Note angle computation in VGT may involve more than just angular displacement value: in VGT angles may be drawn in 3D which requires knowledge and evaluation of supporting vectors.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarAngle


Property detail
---------------

.. py:property:: input_angle
    :canonical: ansys.stk.core.vgt.CalculationToolScalarAngle.input_angle
    :type: IVectorGeometryToolAngle

    The input angle, which is a VGT angle component. Note angle computation in VGT may involve more than just angular displacement value: in VGT angles may be drawn in 3D which requires knowledge and evaluation of supporting vectors.


