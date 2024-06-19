ISiteWaypoint
=============

.. py:class:: ISiteWaypoint

   object
   
   Interface used to access the options for a waypoint site.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteWaypoint


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypoint.latitude
    :type: typing.Any

    Gets or sets the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypoint.longitude
    :type: typing.Any

    Gets or sets the waypoint longitude.


Method detail
-------------





.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypoint.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

