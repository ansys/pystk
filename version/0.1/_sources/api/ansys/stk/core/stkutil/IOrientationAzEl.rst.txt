IOrientationAzEl
================

.. py:class:: ansys.stk.core.stkutil.IOrientationAzEl

   Bases: IOrientation

   Interface for AzEl orientation method.

.. py:currentmodule:: IOrientationAzEl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationAzEl.azimuth`
              - Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationAzEl.elevation`
              - Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientationAzEl.about_boresight`
              - Determine orientation of the X and Y axes with respect to the parent's reference frame.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrientationAzEl


Property detail
---------------

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkutil.IOrientationAzEl.azimuth
    :type: typing.Any

    Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.

.. py:property:: elevation
    :canonical: ansys.stk.core.stkutil.IOrientationAzEl.elevation
    :type: typing.Any

    Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.

.. py:property:: about_boresight
    :canonical: ansys.stk.core.stkutil.IOrientationAzEl.about_boresight
    :type: AzElAboutBoresight

    Determine orientation of the X and Y axes with respect to the parent's reference frame.


