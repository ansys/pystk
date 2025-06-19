IOrientationYPRAngles
=====================

.. py:class:: ansys.stk.core.stkutil.IOrientationYPRAngles

   Bases: IOrientation

   Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

.. py:currentmodule:: IOrientationYPRAngles

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationYPRAngles.sequence`
              - YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationYPRAngles.yaw`
              - Yaw angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationYPRAngles.pitch`
              - Pitch angle. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationYPRAngles.roll`
              - Roll angle. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrientationYPRAngles


Property detail
---------------

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.IOrientationYPRAngles.sequence
    :type: YPRAnglesSequence

    YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.

.. py:property:: yaw
    :canonical: ansys.stk.core.stkutil.IOrientationYPRAngles.yaw
    :type: typing.Any

    Yaw angle. Uses Angle Dimension.

.. py:property:: pitch
    :canonical: ansys.stk.core.stkutil.IOrientationYPRAngles.pitch
    :type: typing.Any

    Pitch angle. Uses Angle Dimension.

.. py:property:: roll
    :canonical: ansys.stk.core.stkutil.IOrientationYPRAngles.roll
    :type: typing.Any

    Roll angle. Uses Angle Dimension.


