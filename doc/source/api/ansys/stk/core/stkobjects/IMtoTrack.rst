IMtoTrack
=========

.. py:class:: IMtoTrack

   object
   
   List of MTO tracks with basic information about each.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~interpolate`
            * - :py:meth:`~id`
            * - :py:meth:`~points`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoTrack


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IMtoTrack.name
    :type: str

    Gets or sets the name assigned to the track.

.. py:property:: interpolate
    :canonical: ansys.stk.core.stkobjects.IMtoTrack.interpolate
    :type: bool

    Opt whether the track's position will be linearly interpolated between points, or will only be displayed at the defined points at the defined times.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IMtoTrack.id
    :type: int

    Get the identification number of the track.

.. py:property:: points
    :canonical: ansys.stk.core.stkobjects.IMtoTrack.points
    :type: "IAgMtoTrackPointCollection"

    Get the collection of MTO track points.


