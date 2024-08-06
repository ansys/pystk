MtoTrack
========

.. py:class:: ansys.stk.core.stkobjects.MtoTrack

   List of MTO tracks with basic information about each.

.. py:currentmodule:: MtoTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrack.name`
              - Gets or sets the name assigned to the track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrack.interpolate`
              - Opt whether the track's position will be linearly interpolated between points, or will only be displayed at the defined points at the defined times.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrack.id`
              - Get the identification number of the track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrack.points`
              - Get the collection of MTO track points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoTrack


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.MtoTrack.name
    :type: str

    Gets or sets the name assigned to the track.

.. py:property:: interpolate
    :canonical: ansys.stk.core.stkobjects.MtoTrack.interpolate
    :type: bool

    Opt whether the track's position will be linearly interpolated between points, or will only be displayed at the defined points at the defined times.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.MtoTrack.id
    :type: int

    Get the identification number of the track.

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.MtoTrack.points
    :type: MtoTrackPointCollection

    Get the collection of MTO track points.


