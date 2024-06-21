IVectorGeometryToolAxesPlugin
=============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin

   object
   
   A VGT axes plugin.

.. py:currentmodule:: IVectorGeometryToolAxesPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.reset`
              - Reset the plugin.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.set_property`
              - Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.get_property`
              - Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.prog_id`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.display_name`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.available_properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesPlugin


Property detail
---------------

.. py:property:: prog_id
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.prog_id
    :type: str

    A programmatic ID associated with the component.

.. py:property:: display_name
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.display_name
    :type: str

    Plugin's Display Name associated with the COM plugin.

.. py:property:: available_properties
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.available_properties
    :type: list

    An array of names of the properties that can be used to configure the plugin.


Method detail
-------------




.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.reset

    Reset the plugin.

    :Returns:

        :obj:`~None`

.. py:method:: set_property(self, name: str, value: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.set_property

    Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.

    :Parameters:

    **name** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_property(self, name: str) -> str
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesPlugin.get_property

    Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~str`

