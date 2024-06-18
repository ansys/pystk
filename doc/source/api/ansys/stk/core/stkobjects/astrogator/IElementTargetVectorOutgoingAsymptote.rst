IElementTargetVectorOutgoingAsymptote
=====================================

.. py:class:: IElementTargetVectorOutgoingAsymptote

   IElement
   
   Properties for Target Vector Outgoing Asymptote elements.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~radius_of_periapsis`
            * - :py:meth:`~c3_energy`
            * - :py:meth:`~ra_outgoing_asymptote`
            * - :py:meth:`~declination_outgoing_asymptote`
            * - :py:meth:`~velocity_azimuth_periapsis`
            * - :py:meth:`~true_anomaly`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementTargetVectorOutgoingAsymptote


Property detail
---------------

.. py:property:: radius_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.radius_of_periapsis
    :type: float

    Radius of Periapsis. Uses Distance Dimension.

.. py:property:: c3_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.c3_energy
    :type: float

    C3Energy (Rate Squared).

.. py:property:: ra_outgoing_asymptote
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.ra_outgoing_asymptote
    :type: typing.Any

    Right Ascension of Incoming Asymptote. Uses Angle Dimension.

.. py:property:: declination_outgoing_asymptote
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.declination_outgoing_asymptote
    :type: typing.Any

    Declination of Incoming Asymptote. Uses Angle Dimension.

.. py:property:: velocity_azimuth_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.velocity_azimuth_periapsis
    :type: typing.Any

    Velocity Azimuth at Periapsis. Uses Angle Dimension.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote.true_anomaly
    :type: typing.Any

    True Anomaly. Uses Angle Dimension.


