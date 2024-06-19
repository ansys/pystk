IConstantDisplayConditionFactory
================================

.. py:class:: IConstantDisplayConditionFactory

   object
   
   A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default constant display condition. display is set to false so when this display condition is assigned to an object, such as a primitive, the object is not rendered.
            * - :py:meth:`~initialize_display`
              - Initialize a constant display condition with the value the display condition evaluates to.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IConstantDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> IConstantDisplayCondition
    :canonical: ansys.stk.core.graphics.IConstantDisplayConditionFactory.initialize

    Initialize a default constant display condition. display is set to false so when this display condition is assigned to an object, such as a primitive, the object is not rendered.

    :Returns:

        :obj:`~IConstantDisplayCondition`

.. py:method:: initialize_display(self, display: bool) -> IConstantDisplayCondition
    :canonical: ansys.stk.core.graphics.IConstantDisplayConditionFactory.initialize_display

    Initialize a constant display condition with the value the display condition evaluates to.

    :Parameters:

    **display** : :obj:`~bool`

    :Returns:

        :obj:`~IConstantDisplayCondition`

