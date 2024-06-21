IAltitudeDisplayCondition
=========================

.. py:class:: ansys.stk.core.graphics.IAltitudeDisplayCondition

   object
   
   Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

.. py:currentmodule:: IAltitudeDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayCondition.minimum_altitude`
            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayCondition.maximum_altitude`
            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayCondition.central_body`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAltitudeDisplayCondition


Property detail
---------------

.. py:property:: minimum_altitude
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayCondition.minimum_altitude
    :type: float

    Gets or sets the minimum altitude of the inclusive altitude interval. Use Double.MinValue to ignore checking the minimum altitude.

.. py:property:: maximum_altitude
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayCondition.maximum_altitude
    :type: float

    Gets or sets the maximum altitude of the inclusive altitude interval. Use Double.MaxValue to ignore checking the maximum altitude.

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayCondition.central_body
    :type: str

    Gets or sets the central body to which the altitude is relative.


