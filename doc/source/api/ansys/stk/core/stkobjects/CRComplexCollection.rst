CRComplexCollection
===================

.. py:class:: ansys.stk.core.stkobjects.CRComplexCollection

   Class defining a collection of complex numbers.

.. py:currentmodule:: CRComplexCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.remove_at`
              - Remove the complex value with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.add`
              - Add and returns a new complex value.
            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.insert_at`
              - Insert and returns a new complex value at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.clear`
              - Clear all complex values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CRComplexCollection._NewEnum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CRComplexCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> CRComplex
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CRComplex`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.remove_at

    Remove the complex value with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, real: float, imaginary: float) -> CRComplex
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.add

    Add and returns a new complex value.

    :Parameters:

    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~CRComplex`

.. py:method:: insert_at(self, index: int, real: float, imaginary: float) -> CRComplex
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.insert_at

    Insert and returns a new complex value at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~CRComplex`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.CRComplexCollection.clear

    Clear all complex values from the collection.

    :Returns:

        :obj:`~None`

