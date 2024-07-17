AtmosphereModel
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.AtmosphereModel

   Bases: 

   Class defining the atmosphere model for a mission, scenario, or procedure.

.. py:currentmodule:: AtmosphereModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.copy`
              - Copy the atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.paste`
              - Paste the atmosphere model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_type_string`
              - Gets or sets the atmosphere model type as a string value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_source`
              - Gets or sets the atmosphere model source.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.mode_as_basic`
              - Get the options for a Basic Atmosphere model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AtmosphereModel


Property detail
---------------

.. py:property:: atmosphere_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_type_string
    :type: str

    Gets or sets the atmosphere model type as a string value.

.. py:property:: atmosphere_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_source
    :type: WIND_ATMOS_MODEL_SOURCE

    Gets or sets the atmosphere model source.

.. py:property:: mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.mode_as_basic
    :type: IAtmosphereModelBasic

    Get the options for a Basic Atmosphere model.


Method detail
-------------






.. py:method:: copy(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.copy

    Copy the atmosphere model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.paste

    Paste the atmosphere model.

    :Returns:

        :obj:`~None`

