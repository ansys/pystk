IOrientationEulerAngles
=======================

.. py:class:: ansys.stk.core.stkutil.IOrientationEulerAngles

   Bases: IOrientation

   Interface for Euler Angles orientation method.

.. py:currentmodule:: IOrientationEulerAngles

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationEulerAngles.sequence`
              - Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationEulerAngles.a`
              - Euler A angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationEulerAngles.b`
              - Euler b angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationEulerAngles.c`
              - Euler C angle. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrientationEulerAngles


Property detail
---------------

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.IOrientationEulerAngles.sequence
    :type: EULER_ORIENTATION_SEQUENCE_TYPE

    Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.

.. py:property:: a
    :canonical: ansys.stk.core.stkutil.IOrientationEulerAngles.a
    :type: typing.Any

    Euler A angle. Uses Angle Dimension.

.. py:property:: b
    :canonical: ansys.stk.core.stkutil.IOrientationEulerAngles.b
    :type: typing.Any

    Euler b angle. Uses Angle Dimension.

.. py:property:: c
    :canonical: ansys.stk.core.stkutil.IOrientationEulerAngles.c
    :type: typing.Any

    Euler C angle. Uses Angle Dimension.


