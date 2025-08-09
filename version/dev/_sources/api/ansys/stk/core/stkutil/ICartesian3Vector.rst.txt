ICartesian3Vector
=================

.. py:class:: ansys.stk.core.stkutil.ICartesian3Vector

   Represents a cartesian 3-D vector.

.. py:currentmodule:: ICartesian3Vector

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.get`
              - Return cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.set`
              - Set cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.to_array`
              - Return coordinates as an array.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.x`
              - X coordinate.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.y`
              - Y coordinate.
            * - :py:attr:`~ansys.stk.core.stkutil.ICartesian3Vector.z`
              - Z coordinate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ICartesian3Vector


Property detail
---------------

.. py:property:: x
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.x
    :type: float

    X coordinate.

.. py:property:: y
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.y
    :type: float

    Y coordinate.

.. py:property:: z
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.z
    :type: float

    Z coordinate.


Method detail
-------------

.. py:method:: get(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.get

    Return cartesian vector.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

.. py:method:: set(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.set

    Set cartesian vector.

    :Parameters:

        **x** : :obj:`~float`

        **y** : :obj:`~float`

        **z** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkutil.ICartesian3Vector.to_array

    Return coordinates as an array.

    :Returns:

        :obj:`~list`







