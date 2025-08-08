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

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model`
              - Get the current antenna model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name`
              - Get or set the current antenna model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.frequency`
              - Get or set the beam frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.identifier`
              - Get or set the antenna beam identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.is_active`
              - Get or set the beam active flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.orientation`
              - Get the antenna orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models`
              - Get an array of supported antenna model names.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaBeam


Property detail
---------------

.. py:property:: antenna_model
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model
    :type: IAntennaModel

    Get the current antenna model.

.. py:property:: antenna_model_name
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.antenna_model_name
    :type: str

    Get or set the current antenna model by name.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.frequency
    :type: float

    Get or set the beam frequency.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.identifier
    :type: str

    Get or set the antenna beam identifier.

.. py:property:: is_active
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.is_active
    :type: bool

    Get or set the beam active flag.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.orientation
    :type: IOrientation

    Get the antenna orientation.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: supported_antenna_models
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.supported_antenna_models
    :type: list

    Get an array of supported antenna model names.


Method detail
-------------















.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaBeam.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`


