IModelTransformation
====================

.. py:class:: IModelTransformation

   object
   
   A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~current_value`
            * - :py:meth:`~minimum_value`
            * - :py:meth:`~maximum_value`
            * - :py:meth:`~default_value`
            * - :py:meth:`~range`
            * - :py:meth:`~name`
            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IModelTransformation


Property detail
---------------

.. py:property:: current_value
    :canonical: ansys.stk.core.graphics.IModelTransformation.current_value
    :type: float

    Gets or sets the current value of the transformation. The current value of the transformation will be reflected in the geometry of the model primitive that it is associated with.

.. py:property:: minimum_value
    :canonical: ansys.stk.core.graphics.IModelTransformation.minimum_value
    :type: float

    Gets the minimum value of the transformation.

.. py:property:: maximum_value
    :canonical: ansys.stk.core.graphics.IModelTransformation.maximum_value
    :type: float

    Gets the maximum value of the transformation.

.. py:property:: default_value
    :canonical: ansys.stk.core.graphics.IModelTransformation.default_value
    :type: float

    Gets the default value of the transformation. The current value property of the transformation will have this value when the model primitive is initialized.

.. py:property:: range
    :canonical: ansys.stk.core.graphics.IModelTransformation.range
    :type: float

    Gets the value range of the transformation. Equivalent to the difference of the maximum value and minimum value properties.

.. py:property:: name
    :canonical: ansys.stk.core.graphics.IModelTransformation.name
    :type: str

    Gets the name of the transformation.

.. py:property:: type
    :canonical: ansys.stk.core.graphics.IModelTransformation.type
    :type: MODEL_TRANSFORMATION_TYPE

    Gets the model transformation type associated with the transformation.


