IScatteringPointProviderCollectionElement
=========================================

.. py:class:: ansys.stk.core.stkobjects.IScatteringPointProviderCollectionElement

   object
   
   Provide access to the properties and methods defining an entry in the scattering point provider collection.

.. py:currentmodule:: IScatteringPointProviderCollectionElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollectionElement.enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollectionElement.scattering_point_provider`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointProviderCollectionElement


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollectionElement.enabled
    :type: bool

    Gets or sets whether or not the scattering point provider is active.

.. py:property:: scattering_point_provider
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollectionElement.scattering_point_provider
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the scattering point provider component.


