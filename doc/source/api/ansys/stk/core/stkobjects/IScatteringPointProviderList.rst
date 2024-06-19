IScatteringPointProviderList
============================

.. py:class:: IScatteringPointProviderList

   object
   
   Provide access to the properties and methods defining a scattering point provider list.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`
            * - :py:meth:`~point_providers`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointProviderList


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderList.name
    :type: str

    Gets the scattering point provider list name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderList.type
    :type: SCATTERING_POINT_PROVIDER_LIST_TYPE

    Gets the scattering point provider list type enumeration.

.. py:property:: point_providers
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderList.point_providers
    :type: IAgScatteringPointProviderCollection

    Gets the scattering point provider list collection.


