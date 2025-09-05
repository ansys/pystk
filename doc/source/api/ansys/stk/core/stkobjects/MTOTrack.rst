MTOTrack
========

.. py:class:: ansys.stk.core.stkobjects.MTOTrack

   List of MTO tracks with basic information about each.

.. py:currentmodule:: MTOTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrack.identifier`
              - Get the identification number of the track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrack.interpolate`
              - Opt whether the track's position will be linearly interpolated between points, or will only be displayed at the defined points at the defined times.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrack.name`
              - Get or set the name assigned to the track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrack.points`
              - Get the collection of MTO track points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOTrack


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.MTOTrack.identifier
    :type: int

    Get the identification number of the track.

.. py:property:: interpolate
    :canonical: ansys.stk.core.stkobjects.MTOTrack.interpolate
    :type: bool

    Opt whether the track's position will be linearly interpolated between points, or will only be displayed at the defined points at the defined times.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.MTOTrack.name
    :type: str

    Get or set the name assigned to the track.

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.MTOTrack.points
    :type: MTOTrackPointCollection

    Get the collection of MTO track points.


