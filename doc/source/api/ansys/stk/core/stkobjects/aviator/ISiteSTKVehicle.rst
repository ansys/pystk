ISiteSTKVehicle
===============

.. py:class:: ISiteSTKVehicle

   object
   
   Interface used to access the options for a STK Vehicle site.

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

            * - :py:meth:`~object_name`
            * - :py:meth:`~valid_object_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteSTKVehicle


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKVehicle.object_name
    :type: str

    Gets or sets the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKVehicle.valid_object_names
    :type: list

    Returns the valid object names.


Method detail
-------------




.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKVehicle.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

