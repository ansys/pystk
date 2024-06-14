ICartesian2Vector
=================

.. py:class:: ICartesian2Vector

   object
   
   Represents a cartesian 2-D vector.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get`
              - Return cartesian vector.
            * - :py:meth:`~set`
              - Set cartesian vector.
            * - :py:meth:`~to_array`
              - Return coordinates as an array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~x`
            * - :py:meth:`~y`


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

    Return cartesian vector.

    :Returns:

        :obj:`~typing.Tuple[float, float]`

.. py:method:: set(self, x:float, y:float) -> None

    Set cartesian vector.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list

    Return coordinates as an array.

    :Returns:

        :obj:`~list`

