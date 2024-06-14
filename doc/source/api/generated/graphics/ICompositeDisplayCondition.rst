ICompositeDisplayCondition
==========================

.. py:class:: ICompositeDisplayCondition

   object
   
   A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the condition at the given zero-based index.
            * - :py:meth:`~reserve`
              - Request enough memory for the composite to contain at least count display conditions. count will not be affected but capacity may be.
            * - :py:meth:`~add_with_negate`
              - Add a display condition to the end of the composite.
            * - :py:meth:`~add`
              - Add a display condition to the end of the composite.
            * - :py:meth:`~insert_with_negate`
              - Insert a display condition at the given zero-based index, shifting existing display conditions.
            * - :py:meth:`~insert`
              - Insert a display condition at the given zero-based index, shifting existing display conditions.
            * - :py:meth:`~remove`
              - Remove a display condition from the composite.
            * - :py:meth:`~remove_at`
              - Remove the display condition at the given zero-based index, shifting existing display conditions.
            * - :py:meth:`~clear`
              - Remove all display conditions from the composite.
            * - :py:meth:`~get_negate`
              - Determine if a logical not operation is applied to a display condition in the composite.
            * - :py:meth:`~set_negate`
              - Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.
            * - :py:meth:`~get_negate_at`
              - Determine if a logical not operation is applied to a display condition in the composite.
            * - :py:meth:`~set_negate_at`
              - Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~capacity`
            * - :py:meth:`~logic_operation`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICompositeDisplayCondition


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ICompositeDisplayCondition.count
    :type: int

    Gets the number of display conditions in the composite.

.. py:property:: capacity
    :canonical: ansys.stk.core.graphics.ICompositeDisplayCondition.capacity
    :type: int

    Gets the number of display conditions for which memory has been allocated. This will always be greater or equal to count.

.. py:property:: logic_operation
    :canonical: ansys.stk.core.graphics.ICompositeDisplayCondition.logic_operation
    :type: "BINARY_LOGIC_OPERATION"

    Gets or sets the binary logic operation applied to all display conditions in the composite when the composite is evaluated. To combine logical and and or operations in the same expression, create composites containing composites.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.ICompositeDisplayCondition._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection.


Method detail
-------------





.. py:method:: item(self, index:int) -> "IDisplayCondition"

    Return the condition at the given zero-based index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IDisplayCondition"`


.. py:method:: reserve(self, count:int) -> None

    Request enough memory for the composite to contain at least count display conditions. count will not be affected but capacity may be.

    :Parameters:

    **count** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_with_negate(self, displayCondition:"IDisplayCondition", negate:bool) -> None

    Add a display condition to the end of the composite.

    :Parameters:

    **displayCondition** : :obj:`~"IDisplayCondition"`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, displayCondition:"IDisplayCondition") -> None

    Add a display condition to the end of the composite.

    :Parameters:

    **displayCondition** : :obj:`~"IDisplayCondition"`

    :Returns:

        :obj:`~None`

.. py:method:: insert_with_negate(self, index:int, displayCondition:"IDisplayCondition", negate:bool) -> None

    Insert a display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`
    **displayCondition** : :obj:`~"IDisplayCondition"`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: insert(self, index:int, displayCondition:"IDisplayCondition") -> None

    Insert a display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`
    **displayCondition** : :obj:`~"IDisplayCondition"`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, displayCondition:"IDisplayCondition") -> None

    Remove a display condition from the composite.

    :Parameters:

    **displayCondition** : :obj:`~"IDisplayCondition"`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index:int) -> None

    Remove the display condition at the given zero-based index, shifting existing display conditions.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None

    Remove all display conditions from the composite.

    :Returns:

        :obj:`~None`

.. py:method:: get_negate(self, displayCondition:"IDisplayCondition") -> bool

    Determine if a logical not operation is applied to a display condition in the composite.

    :Parameters:

    **displayCondition** : :obj:`~"IDisplayCondition"`

    :Returns:

        :obj:`~bool`

.. py:method:: set_negate(self, displayCondition:"IDisplayCondition", negate:bool) -> None

    Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    :Parameters:

    **displayCondition** : :obj:`~"IDisplayCondition"`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: get_negate_at(self, index:int) -> bool

    Determine if a logical not operation is applied to a display condition in the composite.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~bool`

.. py:method:: set_negate_at(self, index:int, negate:bool) -> None

    Set if a logical not operation is applied to a display condition in the composite when the composite is evaluated.

    :Parameters:

    **index** : :obj:`~int`
    **negate** : :obj:`~bool`

    :Returns:

        :obj:`~None`

