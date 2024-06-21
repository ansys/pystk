ICartesian2Vector
=================

.. py:class:: ansys.stk.core.stkutil.ICartesian2Vector

   object
   
   Represents a cartesian 2-D vector.

.. py:currentmodule:: ICartesian2Vector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian2Vector.get`
              - Return cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian2Vector.set`
              - Set cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian2Vector.to_array`
              - Return coordinates as an array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian2Vector.x`
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian2Vector.y`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ICartesian2Vector


Property detail
---------------

.. py:property:: x
    :canonical: ansys.stk.core.stkutil.ICartesian2Vector.x
    :type: float

    X coordinate.

.. py:property:: y
    :canonical: ansys.stk.core.stkutil.ICartesian2Vector.y
    :type: float

    Y coordinate.


Method detail
-------------





.. py:method:: get(self) -> typing.Tuple[float, float]
    :canonical: ansys.stk.core.stkutil.ICartesian2Vector.get

    Return cartesian vector.

    :Returns:

        :obj:`~typing.Tuple[float, float]`

.. py:method:: set(self, x: float, y: float) -> None
    :canonical: ansys.stk.core.stkutil.ICartesian2Vector.set

    Set cartesian vector.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkutil.ICartesian2Vector.to_array

    Return coordinates as an array.

    :Returns:

        :obj:`~list`

