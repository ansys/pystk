ModelTransformation
===================

.. py:class:: ansys.stk.core.graphics.ModelTransformation

   A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

.. py:currentmodule:: ModelTransformation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.current_value`
              - Gets or sets the current value of the transformation. The current value of the transformation will be reflected in the geometry of the model primitive that it is associated with.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.minimum_value`
              - Gets the minimum value of the transformation.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.maximum_value`
              - Gets the maximum value of the transformation.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.default_value`
              - Gets the default value of the transformation. The current value property of the transformation will have this value when the model primitive is initialized.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.range`
              - Gets the value range of the transformation. Equivalent to the difference of the maximum value and minimum value properties.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.name`
              - Gets the name of the transformation.
            * - :py:attr:`~ansys.stk.core.graphics.ModelTransformation.type`
              - Gets the model transformation type associated with the transformation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ModelTransformation


Property detail
---------------

.. py:property:: current_value
    :canonical: ansys.stk.core.graphics.ModelTransformation.current_value
    :type: float

    Gets or sets the current value of the transformation. The current value of the transformation will be reflected in the geometry of the model primitive that it is associated with.

.. py:property:: minimum_value
    :canonical: ansys.stk.core.graphics.ModelTransformation.minimum_value
    :type: float

    Gets the minimum value of the transformation.

.. py:property:: maximum_value
    :canonical: ansys.stk.core.graphics.ModelTransformation.maximum_value
    :type: float

    Gets the maximum value of the transformation.

.. py:property:: default_value
    :canonical: ansys.stk.core.graphics.ModelTransformation.default_value
    :type: float

    Gets the default value of the transformation. The current value property of the transformation will have this value when the model primitive is initialized.

.. py:property:: range
    :canonical: ansys.stk.core.graphics.ModelTransformation.range
    :type: float

    Gets the value range of the transformation. Equivalent to the difference of the maximum value and minimum value properties.

.. py:property:: name
    :canonical: ansys.stk.core.graphics.ModelTransformation.name
    :type: str

    Gets the name of the transformation.

.. py:property:: type
    :canonical: ansys.stk.core.graphics.ModelTransformation.type
    :type: ModelTransformationType

    Gets the model transformation type associated with the transformation.


