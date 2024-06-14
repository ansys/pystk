IVectorGeometryToolVectorPlugin
===============================

.. py:class:: IVectorGeometryToolVectorPlugin

   object
   
   A VGT vector plugin.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reset`
              - Reset the plugin.
            * - :py:meth:`~set_property`
              - Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.
            * - :py:meth:`~get_property`
              - Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~prog_id`
            * - :py:meth:`~display_name`
            * - :py:meth:`~available_properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorPlugin


Property detail
---------------

.. py:property:: prog_id
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPlugin.prog_id
    :type: str

    A programmatic ID associated with the component.

.. py:property:: display_name
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPlugin.display_name
    :type: str

    Plugin's Display Name associated with the COM plugin.

.. py:property:: available_properties
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPlugin.available_properties
    :type: list

    An array of names of the properties that can be used to configure the plugin.


Method detail
-------------




.. py:method:: reset(self) -> None

    Reset the plugin.

    :Returns:

        :obj:`~None`

.. py:method:: set_property(self, name:str, value:str) -> None

    Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.

    :Parameters:

    **name** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_property(self, name:str) -> str

    Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~str`

