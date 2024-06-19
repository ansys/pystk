IRadarCrossSection
==================

.. py:class:: IRadarCrossSection

   object
   
   Provide access to the properties and methods defining radar cross section.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_model`
              - Set the current RCS model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_models`
            * - :py:meth:`~model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSection


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSection.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSection.model
    :type: IAgRadarCrossSectionModel

    Gets the current RCS model.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSection.set_model

    Set the current RCS model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


