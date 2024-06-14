IVehicleSGP4OnlineLoad
======================

.. py:class:: IVehicleSGP4OnlineLoad

   IVehicleSGP4LoadData
   
   Interface for SGP4 propagator. Loads segments from online.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_segs_from_online`
              - Return an array with all segments related to the supplied SSC number.
            * - :py:meth:`~add_segs_from_online`
              - Accept an array of segments to add.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~load_newest`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSGP4OnlineLoad


Property detail
---------------

.. py:property:: load_newest
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4OnlineLoad.load_newest
    :type: bool

    Use this is you want to grab the latest segment with the given SSC number.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4OnlineLoad.start_time
    :type: typing.Any

    Start time to look for segments. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4OnlineLoad.stop_time
    :type: typing.Any

    Stop time to look for segments. Uses DateFormat Dimension.


Method detail
-------------







.. py:method:: get_segs_from_online(self, SSCNum:str) -> list

    Return an array with all segments related to the supplied SSC number.

    :Parameters:

    **SSCNum** : :obj:`~str`

    :Returns:

        :obj:`~list`

.. py:method:: add_segs_from_online(self, segments:list) -> None

    Accept an array of segments to add.

    :Parameters:

    **segments** : :obj:`~list`

    :Returns:

        :obj:`~None`

