CompositeDisplayCondition
=========================

.. py:class:: ansys.stk.core.graphics.CompositeDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

.. py:currentmodule:: CompositeDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.item`
              - Return the condition at the given zero-based index.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.reserve`
              - Request enough memory for the composite to contain at least count display conditions. count will not be affected but capacity may be.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.add_with_negate`
              - Add a display condition to the end of the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.add`
              - Add a display condition to the end of the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.insert_with_negate`
              - Insert a display condition at the given zero-based index, shifting existing display conditions.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.insert`
              - Insert a display condition at the given zero-based index, shifting existing display conditions.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.remove`
              - Remove a display condition from the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.remove_at`
              - Remove the display condition at the given zero-based index, shifting existing display conditions.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.clear`
              - Remove all display conditions from the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.get_negate`
              - Determine if a logical not operation is applied to a display condition in the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.set_negate`
              - Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.get_negate_at`
              - Determine if a logical not operation is applied to a display condition in the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.set_negate_at`
              - Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.count`
              - Gets the number of display conditions in the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.capacity`
              - Gets the number of display conditions for which memory has been allocated. This will always be greater or equal to count.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition.logic_operation`
              - Gets or sets the binary logic operation applied to all display conditions in the composite when the composite is evaluated. To combine logical and and or operations in the same expression, create composites containing composites.
            * - :py:attr:`~ansys.stk.core.graphics.CompositeDisplayCondition._NewEnum`
              - Returns an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CompositeDisplayCondition


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.count
    :type: int

    Gets the number of display conditions in the composite.

.. py:property:: capacity
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.capacity
    :type: int

    Gets the number of display conditions for which memory has been allocated. This will always be greater or equal to count.

.. py:property:: logic_operation
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.logic_operation
    :type: BINARY_LOGIC_OPERATION

    Gets or sets the binary logic operation applied to all display conditions in the composite when the composite is evaluated. To combine logical and and or operations in the same expression, create composites containing composites.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection.


Method detail
-------------





.. py:method:: item(self, index: int) -> IDisplayCondition
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.item

    Return the condition at the given zero-based index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDisplayCondition`


.. py:method:: reserve(self, count: int) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.reserve

    Request enough memory for the composite to contain at least count display conditions. count will not be affected but capacity may be.

    :Parameters:

    **count** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_with_negate(self, displayCondition: IDisplayCondition, negate: bool) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.add_with_negate

    Add a display condition to the end of the composite.

    :Parameters:

    **displayCondition** : :obj:`~IDisplayCondition`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, displayCondition: IDisplayCondition) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.add

    Add a display condition to the end of the composite.

    :Parameters:

    **displayCondition** : :obj:`~IDisplayCondition`

    :Returns:

        :obj:`~None`

.. py:method:: insert_with_negate(self, index: int, displayCondition: IDisplayCondition, negate: bool) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.insert_with_negate

    Insert a display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`
    **displayCondition** : :obj:`~IDisplayCondition`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: insert(self, index: int, displayCondition: IDisplayCondition) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.insert

    Insert a display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`
    **displayCondition** : :obj:`~IDisplayCondition`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, displayCondition: IDisplayCondition) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.remove

    Remove a display condition from the composite.

    :Parameters:

    **displayCondition** : :obj:`~IDisplayCondition`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.remove_at

    Remove the display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.clear

    Remove all display conditions from the composite.

    :Returns:

        :obj:`~None`

.. py:method:: get_negate(self, displayCondition: IDisplayCondition) -> bool
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.get_negate

    Determine if a logical not operation is applied to a display condition in the composite.

    :Parameters:

    **displayCondition** : :obj:`~IDisplayCondition`

    :Returns:

        :obj:`~bool`

.. py:method:: set_negate(self, displayCondition: IDisplayCondition, negate: bool) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.set_negate

    Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    :Parameters:

    **displayCondition** : :obj:`~IDisplayCondition`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: get_negate_at(self, index: int) -> bool
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.get_negate_at

    Determine if a logical not operation is applied to a display condition in the composite.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~bool`

.. py:method:: set_negate_at(self, index: int, negate: bool) -> None
    :canonical: ansys.stk.core.graphics.CompositeDisplayCondition.set_negate_at

    Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    :Parameters:

    **index** : :obj:`~int`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

