ICalculationToolScalarVectorComponent
=====================================

.. py:class:: ICalculationToolScalarVectorComponent

   object
   
   The specified component of a vector when resolved in the specified axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~input_vector`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~component`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarVectorComponent


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarVectorComponent.input_vector
    :type: IAgCrdnVector

    Vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarVectorComponent.reference_axes
    :type: IAgCrdnAxes

    Axes used to resolve the vector's components.

.. py:property:: component
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarVectorComponent.component
    :type: VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE

    The component of the vector to return as the value of the scalar.


