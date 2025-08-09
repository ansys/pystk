SiteSTKVehicle
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteSTKVehicle

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a STK Vehicle site.

.. py:currentmodule:: SiteSTKVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.object_name`
              - Get or set the object name to link to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.valid_object_names`
              - Return the valid object names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteSTKVehicle


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.object_name
    :type: str

    Get or set the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.valid_object_names
    :type: list

    Return the valid object names.


Method detail
-------------

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKVehicle.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`




