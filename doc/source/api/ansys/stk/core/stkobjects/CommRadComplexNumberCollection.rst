CommRadComplexNumberCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.CommRadComplexNumberCollection

   Class defining a collection of complex numbers.

.. py:currentmodule:: CommRadComplexNumberCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.remove_at`
              - Remove the complex value with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.add`
              - Add and returns a new complex value.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.insert_at`
              - Insert and returns a new complex value at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.clear`
              - Clear all complex values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommRadComplexNumberCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> CommRadComplexNumber
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CommRadComplexNumber`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.remove_at

    Remove the complex value with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, real: float, imaginary: float) -> CommRadComplexNumber
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.add

    Add and returns a new complex value.

    :Parameters:

    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~CommRadComplexNumber`

.. py:method:: insert_at(self, index: int, real: float, imaginary: float) -> CommRadComplexNumber
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.insert_at

    Insert and returns a new complex value at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~CommRadComplexNumber`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.CommRadComplexNumberCollection.clear

    Clear all complex values from the collection.

    :Returns:

        :obj:`~None`

