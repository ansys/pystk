IRadarClutterMap
================

.. py:class:: IRadarClutterMap

   object
   
   Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar clutter map.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_model`
              - Set the current clutter map model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_models`
            * - :py:meth:`~model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterMap


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMap.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMap.model
    :type: IAgRadarClutterMapModel

    Gets the current clutter map model.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMap.set_model

    Set the current clutter map model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


