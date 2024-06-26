IProfileChangeManeuverType
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType

   IProfile
   
   Properties for a Change Maneuver Type profile.

.. py:currentmodule:: IProfileChangeManeuverType

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.segment`
              - Gets or sets the targeted maneuver segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.maneuver_type`
              - Gets or sets the new maneuver type for the targeted segment.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangeManeuverType


Property detail
---------------

.. py:property:: segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.segment
    :type: IMissionControlSequenceManeuver

    Gets or sets the targeted maneuver segment.

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.maneuver_type
    :type: MANEUVER_TYPE

    Gets or sets the new maneuver type for the targeted segment.


