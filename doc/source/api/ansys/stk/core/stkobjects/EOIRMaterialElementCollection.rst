EOIRMaterialElementCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.EOIRMaterialElementCollection

   Collection of material elements.

.. py:currentmodule:: EOIRMaterialElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.EOIRMaterialElementCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.EOIRMaterialElementCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.EOIRMaterialElementCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import EOIRMaterialElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.EOIRMaterialElementCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.EOIRMaterialElementCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> EOIRMaterialElement
    :canonical: ansys.stk.core.stkobjects.EOIRMaterialElementCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~EOIRMaterialElement`


