IRadarClutter
=============

.. py:class:: ansys.stk.core.stkobjects.IRadarClutter

   object
   
   Interface which defines a radar's clutter.

.. py:currentmodule:: IRadarClutter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutter.enabled`
              - Gets or sets whether clutter is enabled or disabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutter.scattering_point_provider_list`
              - Gets the link/embed controller for managing the scattering point provider list component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutter


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IRadarClutter.enabled
    :type: bool

    Gets or sets whether clutter is enabled or disabled.

.. py:property:: scattering_point_provider_list
    :canonical: ansys.stk.core.stkobjects.IRadarClutter.scattering_point_provider_list
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the scattering point provider list component.


