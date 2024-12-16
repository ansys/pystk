AntennaModelApertureCircularUniform
===================================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a circular uniform aperture antenna model.

.. py:currentmodule:: AntennaModelApertureCircularUniform

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.compute_mainlobe_gain`
              - Gets or sets the option for computing the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.mainlobe_gain`
              - Gets or sets the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.backlobe_gain`
              - Gets or sets the backlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.efficiency`
              - Gets or sets the efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.use_backlobe_as_mainlobe_atten`
              - Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.input_type`
              - Gets or sets the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.diameter`
              - Gets or sets the diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.beamwidth`
              - Gets or sets the beamwidth.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelApertureCircularUniform


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.input_type
    :type: CircularApertureInputType

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.


