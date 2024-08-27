ScatteringPointProviderList
===========================

.. py:class:: ansys.stk.core.stkobjects.ScatteringPointProviderList

   Bases: :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a scattering point provider list.

.. py:currentmodule:: ScatteringPointProviderList

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderList.name`
              - Gets the scattering point provider list name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderList.type`
              - Gets the scattering point provider list type enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderList.point_providers`
              - Gets the scattering point provider list collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScatteringPointProviderList


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderList.name
    :type: str

    Gets the scattering point provider list name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderList.type
    :type: SCATTERING_POINT_PROVIDER_LIST_TYPE

    Gets the scattering point provider list type enumeration.

.. py:property:: point_providers
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderList.point_providers
    :type: ScatteringPointProviderCollection

    Gets the scattering point provider list collection.


