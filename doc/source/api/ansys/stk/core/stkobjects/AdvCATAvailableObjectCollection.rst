AdvCATAvailableObjectCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection

   Read-only collection of available objects.

.. py:currentmodule:: AdvCATAvailableObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.get_available_object`
              - Return name, date and type times of the interval at a given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.to_array`
              - Return a two-dimensional array of objects.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.count`
              - Number of items in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AdvCATAvailableObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.count
    :type: int

    Number of items in the collection.


Method detail
-------------


.. py:method:: get_available_object(self, index: int) -> typing.Tuple[typing.Any, typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.get_available_object

    Return name, date and type times of the interval at a given index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any]`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection.to_array

    Return a two-dimensional array of objects.

    :Returns:

        :obj:`~list`

