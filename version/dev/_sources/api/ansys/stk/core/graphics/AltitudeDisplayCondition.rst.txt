AltitudeDisplayCondition
========================

.. py:class:: ansys.stk.core.graphics.AltitudeDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

.. py:currentmodule:: AltitudeDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayCondition.central_body`
              - Get or set the central body to which the altitude is relative.
            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayCondition.maximum_altitude`
              - Get or set the maximum altitude of the inclusive altitude interval. Use Double.MaxValue to ignore checking the maximum altitude.
            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayCondition.minimum_altitude`
              - Get or set the minimum altitude of the inclusive altitude interval. Use Double.MinValue to ignore checking the minimum altitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import AltitudeDisplayCondition


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.AltitudeDisplayCondition.central_body
    :type: str

    Get or set the central body to which the altitude is relative.

.. py:property:: maximum_altitude
    :canonical: ansys.stk.core.graphics.AltitudeDisplayCondition.maximum_altitude
    :type: float

    Get or set the maximum altitude of the inclusive altitude interval. Use Double.MaxValue to ignore checking the maximum altitude.

.. py:property:: minimum_altitude
    :canonical: ansys.stk.core.graphics.AltitudeDisplayCondition.minimum_altitude
    :type: float

    Get or set the minimum altitude of the inclusive altitude interval. Use Double.MinValue to ignore checking the minimum altitude.


