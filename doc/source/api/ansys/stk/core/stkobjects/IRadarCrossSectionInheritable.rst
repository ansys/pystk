IRadarCrossSectionInheritable
=============================

.. py:class:: ansys.stk.core.stkobjects.IRadarCrossSectionInheritable

   object
   
   Provide access to the properties and methods defining a inheritable radar cross section.

.. py:currentmodule:: IRadarCrossSectionInheritable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.set_model`
              - Set the current RCS model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.inherit`
              - Gets or set the option to inherit the radar cross section from the scenario object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.model`
              - Gets the current RCS model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionInheritable


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.inherit
    :type: bool

    Gets or set the option to inherit the radar cross section from the scenario object.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.model
    :type: IRadarCrossSectionModel

    Gets the current RCS model.


Method detail
-------------




.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionInheritable.set_model

    Set the current RCS model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


