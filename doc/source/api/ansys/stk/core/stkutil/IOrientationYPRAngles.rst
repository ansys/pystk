IOrientationYPRAngles
=====================

.. py:class:: IOrientationYPRAngles

   IOrientation
   
   Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sequence`
            * - :py:meth:`~yaw`
            * - :py:meth:`~pitch`
            * - :py:meth:`~roll`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrientationYPRAngles


Property detail
---------------

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.IOrientationYPRAngles.sequence
    :type: YPR_ANGLES_SEQUENCE

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


