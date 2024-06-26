ICRComplexCollection
====================

.. py:class:: ansys.stk.core.stkobjects.ICRComplexCollection

   object
   
   Represents a collection of complex numbers.

.. py:currentmodule:: ICRComplexCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.remove_at`
              - Remove the complex value with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.add`
              - Add and returns a new complex value.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.insert_at`
              - Insert and returns a new complex value at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.clear`
              - Clear all complex values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRComplexCollection._NewEnum`
              - Returns an enumerator for the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICRComplexCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ICRComplex
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICRComplex`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.remove_at

    Remove the complex value with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, real: float, imaginary: float) -> ICRComplex
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.add

    Add and returns a new complex value.

    :Parameters:

    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~ICRComplex`

.. py:method:: insert_at(self, index: int, real: float, imaginary: float) -> ICRComplex
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.insert_at

    Insert and returns a new complex value at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~ICRComplex`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICRComplexCollection.clear

    Clear all complex values from the collection.

    :Returns:

        :obj:`~None`

