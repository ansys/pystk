AntennaModelApertureCircularBesselEnvelope
==========================================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a circular bessel envelope aperture antenna model.

.. py:currentmodule:: AntennaModelApertureCircularBesselEnvelope

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.compute_mainlobe_gain`
              - Gets or sets the option for computing the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.mainlobe_gain`
              - Gets or sets the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.backlobe_gain`
              - Gets or sets the backlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.efficiency`
              - Gets or sets the efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.use_backlobe_as_mainlobe_atten`
              - Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.input_type`
              - Gets or sets the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.diameter`
              - Gets or sets the diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.beamwidth`
              - Gets or sets the beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.function_power`
              - Gets or sets the function power.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.pedestal_level`
              - Gets or sets the pedestal level.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelApertureCircularBesselEnvelope


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.input_type
    :type: CircularApertureInputType

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.

.. py:property:: function_power
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.function_power
    :type: int

    Gets or sets the function power.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope.pedestal_level
    :type: float

    Gets or sets the pedestal level.


