Quantity
========

.. py:class:: ansys.stk.core.stkutil.Quantity

   Object that contains a quantity.

.. py:currentmodule:: Quantity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.convert_to_unit`
              - Change the value in this quantity to the specified unit.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.add`
              - Add the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.subtract`
              - Subtracts the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.multiply_qty`
              - Multiplies the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.divide_qty`
              - Divides the value from the Quantity interface to this interface. The dimensions must be similar.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.dimension`
              - Get the name of the dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.unit`
              - Get the current Unit abbreviation.
            * - :py:attr:`~ansys.stk.core.stkutil.Quantity.value`
              - Get or set the current value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import Quantity


Property detail
---------------

.. py:property:: dimension
    :canonical: ansys.stk.core.stkutil.Quantity.dimension
    :type: str

    Get the name of the dimension.

.. py:property:: unit
    :canonical: ansys.stk.core.stkutil.Quantity.unit
    :type: str

    Get the current Unit abbreviation.

.. py:property:: value
    :canonical: ansys.stk.core.stkutil.Quantity.value
    :type: float

    Get or set the current value.


Method detail
-------------



.. py:method:: convert_to_unit(self, unit_abbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.Quantity.convert_to_unit

    Change the value in this quantity to the specified unit.

    :Parameters:

        **unit_abbrv** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: add(self, quantity: Quantity) -> Quantity
    :canonical: ansys.stk.core.stkutil.Quantity.add

    Add the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.

    :Parameters:

        **quantity** : :obj:`~Quantity`


    :Returns:

        :obj:`~Quantity`

.. py:method:: subtract(self, quantity: Quantity) -> Quantity
    :canonical: ansys.stk.core.stkutil.Quantity.subtract

    Subtracts the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.

    :Parameters:

        **quantity** : :obj:`~Quantity`


    :Returns:

        :obj:`~Quantity`

.. py:method:: multiply_qty(self, quantity: Quantity) -> Quantity
    :canonical: ansys.stk.core.stkutil.Quantity.multiply_qty

    Multiplies the value from the Quantity interface to this interface. Returns a new Quantity. The dimensions must be similar.

    :Parameters:

        **quantity** : :obj:`~Quantity`


    :Returns:

        :obj:`~Quantity`

.. py:method:: divide_qty(self, quantity: Quantity) -> Quantity
    :canonical: ansys.stk.core.stkutil.Quantity.divide_qty

    Divides the value from the Quantity interface to this interface. The dimensions must be similar.

    :Parameters:

        **quantity** : :obj:`~Quantity`


    :Returns:

        :obj:`~Quantity`

