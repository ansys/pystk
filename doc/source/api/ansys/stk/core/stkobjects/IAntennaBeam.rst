IAntennaBeam
============

.. py:class:: ansys.stk.core.stkobjects.IAntennaBeam

   Provide access to an antenna beam.

.. py:currentmodule:: IAntennaBeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.identifier`
              - Gets or sets the antenna beam identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.is_active`
              - Gets or sets the beam active flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.frequency`
              - Gets or sets the beam frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models`
              - Gets an array of supported antenna model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name`
              - Gets or sets the current antenna model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model`
              - Gets the current antenna model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.orientation`
              - Gets the antenna orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.polarization`
              - Gets the polarization.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaBeam


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.identifier
    :type: str

    Gets or sets the antenna beam identifier.

.. py:property:: is_active
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.is_active
    :type: bool

    Gets or sets the beam active flag.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.frequency
    :type: float

    Gets or sets the beam frequency.

.. py:property:: supported_antenna_models
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models
    :type: list

    Gets an array of supported antenna model names.

.. py:property:: antenna_model_name
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name
    :type: str

    Gets or sets the current antenna model by name.

.. py:property:: antenna_model
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model
    :type: IAntennaModel

    Gets the current antenna model.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.orientation
    :type: IOrientation

    Gets the antenna orientation.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.polarization
    :type: IPolarization

    Gets the polarization.


Method detail
-------------















.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~PolarizationType`

    :Returns:

        :obj:`~None`


