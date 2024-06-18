ICRComplexCollection
====================

.. py:class:: ICRComplexCollection

   object
   
   Represents a collection of complex numbers.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns the element in the collection.
            * - :py:meth:`~remove_at`
              - Remove the complex value with the supplied index.
            * - :py:meth:`~add`
              - Add and returns a new complex value.
            * - :py:meth:`~insert_at`
              - Insert and returns a new complex value at the supplied index.
            * - :py:meth:`~clear`
              - Clear all complex values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


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


.. py:method:: item(self, index:int) -> "ICRComplex"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ICRComplex"`


.. py:method:: remove_at(self, index:int) -> None

    Remove the complex value with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, real:float, imaginary:float) -> "ICRComplex"

    Add and returns a new complex value.

    :Parameters:

    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~"ICRComplex"`

.. py:method:: insert_at(self, index:int, real:float, imaginary:float) -> "ICRComplex"

    Insert and returns a new complex value at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **real** : :obj:`~float`
    **imaginary** : :obj:`~float`

    :Returns:

        :obj:`~"ICRComplex"`

.. py:method:: clear(self) -> None

    Clear all complex values from the collection.

    :Returns:

        :obj:`~None`

