ConstantDisplayConditionFactory
===============================

.. py:class:: ansys.stk.core.graphics.ConstantDisplayConditionFactory

   Bases: 

   A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

.. py:currentmodule:: ConstantDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ConstantDisplayConditionFactory.initialize`
              - Initialize a default constant display condition. display is set to false so when this display condition is assigned to an object, such as a primitive, the object is not rendered.
            * - :py:attr:`~ansys.stk.core.graphics.ConstantDisplayConditionFactory.initialize_display`
              - Initialize a constant display condition with the value the display condition evaluates to.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ConstantDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> ConstantDisplayCondition
    :canonical: ansys.stk.core.graphics.ConstantDisplayConditionFactory.initialize

    Initialize a default constant display condition. display is set to false so when this display condition is assigned to an object, such as a primitive, the object is not rendered.

    :Returns:

        :obj:`~ConstantDisplayCondition`

.. py:method:: initialize_display(self, display: bool) -> ConstantDisplayCondition
    :canonical: ansys.stk.core.graphics.ConstantDisplayConditionFactory.initialize_display

    Initialize a constant display condition with the value the display condition evaluates to.

    :Parameters:

    **display** : :obj:`~bool`

    :Returns:

        :obj:`~ConstantDisplayCondition`

