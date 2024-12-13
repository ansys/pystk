WindModel
=========

.. py:class:: ansys.stk.core.stkobjects.aviator.WindModel

   Class defining the wind model for a mission, scenario, or procedure.

.. py:currentmodule:: WindModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.copy`
              - Copy the wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.paste`
              - Paste the wind model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type`
              - Gets or sets the wind model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type_string`
              - Gets or sets the wind model type as a string value. Use this for custom models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_source`
              - Gets or sets the wind model source.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.mode_as_constant`
              - Get the options for a Constant Bearing/Speed wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.mode_as_adds`
              - Get the options for a NOAA ADDS Service wind model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import WindModel


Property detail
---------------

.. py:property:: wind_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type
    :type: WindModelType

    Gets or sets the wind model type.

.. py:property:: wind_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type_string
    :type: str

    Gets or sets the wind model type as a string value. Use this for custom models.

.. py:property:: wind_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_source
    :type: WindAtmosModelSource

    Gets or sets the wind model source.

.. py:property:: mode_as_constant
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.mode_as_constant
    :type: WindModelConstant

    Get the options for a Constant Bearing/Speed wind model.

.. py:property:: mode_as_adds
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.mode_as_adds
    :type: WindModelADDS

    Get the options for a NOAA ADDS Service wind model.


Method detail
-------------









.. py:method:: copy(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.copy

    Copy the wind model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.paste

    Paste the wind model.

    :Returns:

        :obj:`~None`

