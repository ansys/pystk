ProfileChangeManeuverType
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Maneuver Type profile.

.. py:currentmodule:: ProfileChangeManeuverType

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType.segment`
              - Gets or sets the targeted maneuver segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType.maneuver_type`
              - Gets or sets the new maneuver type for the targeted segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileChangeManeuverType


Property detail
---------------

.. py:property:: segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType.segment
    :type: MCSManeuver

    Gets or sets the targeted maneuver segment.

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType.maneuver_type
    :type: MANEUVER_TYPE

    Gets or sets the new maneuver type for the targeted segment.


