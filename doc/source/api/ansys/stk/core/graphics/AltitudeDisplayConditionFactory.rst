AltitudeDisplayConditionFactory
===============================

.. py:class:: ansys.stk.core.graphics.AltitudeDisplayConditionFactory

   Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

.. py:currentmodule:: AltitudeDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize`
              - Initialize a default altitude display condition. With this constructor, an object is always rendered regardless of the camera's altitude.
            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize_with_altitudes`
              - Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...
            * - :py:attr:`~ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize_with_central_body_and_altitudes`
              - Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import AltitudeDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> AltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize

    Initialize a default altitude display condition. With this constructor, an object is always rendered regardless of the camera's altitude.

    :Returns:

        :obj:`~AltitudeDisplayCondition`

.. py:method:: initialize_with_altitudes(self, minimum_altitude: float, maximum_altitude: float) -> AltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize_with_altitudes

    Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...

    :Parameters:

        **minimum_altitude** : :obj:`~float`

        **maximum_altitude** : :obj:`~float`


    :Returns:

        :obj:`~AltitudeDisplayCondition`

.. py:method:: initialize_with_central_body_and_altitudes(self, central_body: str, minimum_altitude: float, maximum_altitude: float) -> AltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.AltitudeDisplayConditionFactory.initialize_with_central_body_and_altitudes

    Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...

    :Parameters:

        **central_body** : :obj:`~str`

        **minimum_altitude** : :obj:`~float`

        **maximum_altitude** : :obj:`~float`


    :Returns:

        :obj:`~AltitudeDisplayCondition`

