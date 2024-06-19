IProfileChangeManeuverType
==========================

.. py:class:: IProfileChangeManeuverType

   IProfile
   
   Properties for a Change Maneuver Type profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~segment`
            * - :py:meth:`~maneuver_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangeManeuverType


Property detail
---------------

.. py:property:: segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.segment
    :type: IAgVAMCSManeuver

    Gets or sets the targeted maneuver segment.

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType.maneuver_type
    :type: MANEUVER_TYPE

    Gets or sets the new maneuver type for the targeted segment.


