IQuantity
=========

.. py:class:: ansys.stk.core.stkutil.IQuantity

   object
   
   Provide helper methods for a quantity.

.. py:currentmodule:: IQuantity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.convert_to_unit`
              - Change the value in this quantity to the specified unit.
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.add`
              - Add the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.subtract`
              - Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.multiply_qty`
              - Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.divide_qty`
              - Divides the value from the IAgQuantity interface to this interface. The dimensions must be similar.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.dimension`
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.unit`
            * - :py:attr:`~ansys.stk.core.stkutil.IQuantity.value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IQuantity


Property detail
---------------

.. py:property:: dimension
    :canonical: ansys.stk.core.stkutil.IQuantity.dimension
    :type: str

    Gets the name of the dimension.

.. py:property:: unit
    :canonical: ansys.stk.core.stkutil.IQuantity.unit
    :type: str

    Get the current Unit abbreviation.

.. py:property:: value
    :canonical: ansys.stk.core.stkutil.IQuantity.value
    :type: float

    Gets or sets the current value.


Method detail
-------------



.. py:method:: convert_to_unit(self, unitAbbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.IQuantity.convert_to_unit

    Change the value in this quantity to the specified unit.

    :Parameters:

    **unitAbbrv** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: add(self, quantity: IQuantity) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IQuantity.add

    Add the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.

    :Parameters:

    **quantity** : :obj:`~IQuantity`

    :Returns:

        :obj:`~IQuantity`

.. py:method:: subtract(self, quantity: IQuantity) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IQuantity.subtract

    Subtracts the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.

    :Parameters:

    **quantity** : :obj:`~IQuantity`

    :Returns:

        :obj:`~IQuantity`

.. py:method:: multiply_qty(self, quantity: IQuantity) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IQuantity.multiply_qty

    Multiplies the value from the IAgQuantity interface to this interface. Returns a new IAgQuantity. The dimensions must be similar.

    :Parameters:

    **quantity** : :obj:`~IQuantity`

    :Returns:

        :obj:`~IQuantity`

.. py:method:: divide_qty(self, quantity: IQuantity) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IQuantity.divide_qty

    Divides the value from the IAgQuantity interface to this interface. The dimensions must be similar.

    :Parameters:

    **quantity** : :obj:`~IQuantity`

    :Returns:

        :obj:`~IQuantity`

