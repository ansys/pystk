IRadarDopplerClutterFilters
===========================

.. py:class:: IRadarDopplerClutterFilters

   object
   
   Provide access to the properties and methods defining a radar doppler clutter filter.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_mainlobe_clutter`
            * - :py:meth:`~mainlobe_clutter_bandwidth`
            * - :py:meth:`~enable_sidelobe_clutter`
            * - :py:meth:`~sidelobe_clutter_bandwidth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarDopplerClutterFilters


Property detail
---------------

.. py:property:: enable_mainlobe_clutter
    :canonical: ansys.stk.core.stkobjects.IRadarDopplerClutterFilters.enable_mainlobe_clutter
    :type: bool

    Option for enabling/disabling the mainlobe clutter filter.

.. py:property:: mainlobe_clutter_bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarDopplerClutterFilters.mainlobe_clutter_bandwidth
    :type: float

    Gets or sets the mainlobe filter bandwidth.

.. py:property:: enable_sidelobe_clutter
    :canonical: ansys.stk.core.stkobjects.IRadarDopplerClutterFilters.enable_sidelobe_clutter
    :type: bool

    Option for enabling/disabling the sidelobe clutter filter.

.. py:property:: sidelobe_clutter_bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarDopplerClutterFilters.sidelobe_clutter_bandwidth
    :type: float

    Gets or sets the sidelobe filter bandwidth.


