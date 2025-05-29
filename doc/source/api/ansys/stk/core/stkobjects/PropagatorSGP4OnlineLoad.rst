PropagatorSGP4OnlineLoad
========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagatorSGP4LoadData`

   SGP4 propagator. Allows the user to load segments from online.

.. py:currentmodule:: PropagatorSGP4OnlineLoad

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.get_segments_from_online`
              - Return an array with all segments related to the supplied SSC number.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.add_segments_from_online`
              - Accept an array of segments to add.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.load_newest`
              - Use this is you want to grab the latest segment with the given SSC number.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.start_time`
              - Start time to look for segments. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.stop_time`
              - Stop time to look for segments. Uses DateFormat Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4OnlineLoad


Property detail
---------------

.. py:property:: load_newest
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.load_newest
    :type: bool

    Use this is you want to grab the latest segment with the given SSC number.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.start_time
    :type: typing.Any

    Start time to look for segments. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.stop_time
    :type: typing.Any

    Stop time to look for segments. Uses DateFormat Dimension.


Method detail
-------------







.. py:method:: get_segments_from_online(self, ssc_num: str) -> list
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.get_segments_from_online

    Return an array with all segments related to the supplied SSC number.

    :Parameters:

        **ssc_num** : :obj:`~str`


    :Returns:

        :obj:`~list`

.. py:method:: add_segments_from_online(self, segments: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad.add_segments_from_online

    Accept an array of segments to add.

    :Parameters:

        **segments** : :obj:`~list`


    :Returns:

        :obj:`~None`

