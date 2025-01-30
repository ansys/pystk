ProfileSeedFiniteManeuver
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Seed Finite Maneuver profile.

.. py:currentmodule:: ProfileSeedFiniteManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.set_segment`
              - Set the maneuver segment to target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.segment_name`
              - Gets or sets the targeted maneuver segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.leave_all_active_stopping_conditions_active`
              - If true, all active stopping conditions on the seeded maneuver will remain active during run.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileSeedFiniteManeuver


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.segment_name
    :type: str

    Gets or sets the targeted maneuver segment.

.. py:property:: leave_all_active_stopping_conditions_active
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.leave_all_active_stopping_conditions_active
    :type: bool

    If true, all active stopping conditions on the seeded maneuver will remain active during run.


Method detail
-------------



.. py:method:: set_segment(self, mcs_maneuver: MCSManeuver) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver.set_segment

    Set the maneuver segment to target.

    :Parameters:

    **mcs_maneuver** : :obj:`~MCSManeuver`

    :Returns:

        :obj:`~None`



