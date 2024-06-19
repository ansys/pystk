IProfileSeedFiniteManeuver
==========================

.. py:class:: IProfileSeedFiniteManeuver

   IProfile
   
   Properties for a Seed Finite Maneuver segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_segment`
              - Set the maneuver segment to target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~segment_name`
            * - :py:meth:`~leave_all_active_stopping_conditions_active`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileSeedFiniteManeuver


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSeedFiniteManeuver.segment_name
    :type: str

    Gets or sets the targeted maneuver segment.

.. py:property:: leave_all_active_stopping_conditions_active
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSeedFiniteManeuver.leave_all_active_stopping_conditions_active
    :type: bool

    If true, all active stopping conditions on the seeded maneuver will remain active during run.


Method detail
-------------



.. py:method:: set_segment(self, pVAMCSManeuver: IMissionControlSequenceManeuver) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSeedFiniteManeuver.set_segment

    Set the maneuver segment to target.

    :Parameters:

    **pVAMCSManeuver** : :obj:`~IMissionControlSequenceManeuver`

    :Returns:

        :obj:`~None`



