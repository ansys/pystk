ICalculationToolScalarAngle
===========================

.. py:class:: ICalculationToolScalarAngle

   object
   
   Scalar equal to angular displacement obtained from any angle in VGT.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~input_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarAngle


Property detail
---------------

.. py:property:: input_angle
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarAngle.input_angle
    :type: "IAgCrdnAngle"

    The input angle, which is a VGT angle component. Note angle computation in VGT may involve more than just angular displacement value: in VGT angles may be drawn in 3D which requires knowledge and evaluation of supporting vectors.


