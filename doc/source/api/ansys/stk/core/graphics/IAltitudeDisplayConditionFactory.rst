IAltitudeDisplayConditionFactory
================================

.. py:class:: ansys.stk.core.graphics.IAltitudeDisplayConditionFactory

   object
   
   Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

.. py:currentmodule:: IAltitudeDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize`
              - Initialize a default altitude display condition. With this constructor, an object is always rendered regardless of the camera's altitude.
            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize_with_altitudes`
              - Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...
            * - :py:attr:`~ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize_with_central_body_and_altitudes`
              - Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAltitudeDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> IAltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize

    Initialize a default altitude display condition. With this constructor, an object is always rendered regardless of the camera's altitude.

    :Returns:

        :obj:`~IAltitudeDisplayCondition`

.. py:method:: initialize_with_altitudes(self, minimumAltitude: float, maximumAltitude: float) -> IAltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize_with_altitudes

    Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...

    :Parameters:

    **minimumAltitude** : :obj:`~float`
    **maximumAltitude** : :obj:`~float`

    :Returns:

        :obj:`~IAltitudeDisplayCondition`

.. py:method:: initialize_with_central_body_and_altitudes(self, centralBody: str, minimumAltitude: float, maximumAltitude: float) -> IAltitudeDisplayCondition
    :canonical: ansys.stk.core.graphics.IAltitudeDisplayConditionFactory.initialize_with_central_body_and_altitudes

    Initialize an altitude display condition with the inclusive altitude interval [minimumAltitude, maximumAltitude]...

    :Parameters:

    **centralBody** : :obj:`~str`
    **minimumAltitude** : :obj:`~float`
    **maximumAltitude** : :obj:`~float`

    :Returns:

        :obj:`~IAltitudeDisplayCondition`

