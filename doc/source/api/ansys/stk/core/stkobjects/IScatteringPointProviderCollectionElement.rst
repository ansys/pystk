IScatteringPointProviderCollectionElement
=========================================

.. py:class:: IScatteringPointProviderCollectionElement

   object
   
   Provide access to the properties and methods defining an entry in the scattering point provider collection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enabled`
            * - :py:meth:`~scattering_point_provider`


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
    :type: IAgComponentLinkEmbedControl

    Gets the link/embed controller for managing the scattering point provider component.


