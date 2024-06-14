ICalculationToolParameterSetAttitude
====================================

.. py:class:: ICalculationToolParameterSetAttitude

   object
   
   Attitude parameter set contains various representations of attitude of one set of axes relative to another.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~axes`
            * - :py:meth:`~reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetAttitude


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.axes
    :type: "IAgCrdnAxes"

    Get the axes for which attitude representations are computed.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetAttitude.reference_axes
    :type: "IAgCrdnAxes"

    Get the reference axes relative to which attitude representations are computed.


