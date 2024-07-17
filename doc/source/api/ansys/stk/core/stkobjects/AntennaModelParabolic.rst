AntennaModelParabolic
=====================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelParabolic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a parabolic antenna model.

.. py:currentmodule:: AntennaModelParabolic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.input_type`
              - Gets or sets the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.diameter`
              - Gets or sets the diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.beamwidth`
              - Gets or sets the beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.mainlobe_gain`
              - Gets or sets the main-lobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.backlobe_gain`
              - Gets or sets the back-lobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.use_backlobe_as_mainlobe_atten`
              - Gets or sets the use back-lobe gain as main-lobe attenuation flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelParabolic.efficiency`
              - Gets or sets the efficiency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelParabolic


Property detail
---------------

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.input_type
    :type: ANTENNA_MODEL_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.mainlobe_gain
    :type: float

    Gets or sets the main-lobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.backlobe_gain
    :type: float

    Gets or sets the back-lobe gain.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the use back-lobe gain as main-lobe attenuation flag.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelParabolic.efficiency
    :type: float

    Gets or sets the efficiency.


