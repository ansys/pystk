ICalculationToolParameterSetVector
==================================

.. py:class:: ICalculationToolParameterSetVector

   object
   
   Vector parameter set contains various representations of a vector in a reference set of axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vector`
            * - :py:meth:`~reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetVector


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetVector.vector
    :type: "IAgCrdnVector"

    Get the vector for which representations are computed.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetVector.reference_axes
    :type: "IAgCrdnAxes"

    Get the reference axes relative to which representations are computed.


