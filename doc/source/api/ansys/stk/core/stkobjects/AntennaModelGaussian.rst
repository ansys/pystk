AntennaModelGaussian
====================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelGaussian

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a gaussian antenna model.

.. py:currentmodule:: AntennaModelGaussian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.input_type`
              - Get or set the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.diameter`
              - Get or set the diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.beamwidth`
              - Get or set the beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.mainlobe_gain`
              - Get or set the main-lobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.backlobe_gain`
              - Get or set the back-lobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.use_backlobe_as_mainlobe_atten`
              - Get or set the use back-lobe gain as main-lobe attenuation flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelGaussian.efficiency`
              - Get or set the efficiency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelGaussian


Property detail
---------------

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.input_type
    :type: AntennaModelInputType

    Get or set the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.diameter
    :type: float

    Get or set the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.beamwidth
    :type: typing.Any

    Get or set the beamwidth.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.mainlobe_gain
    :type: float

    Get or set the main-lobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.backlobe_gain
    :type: float

    Get or set the back-lobe gain.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.use_backlobe_as_mainlobe_atten
    :type: bool

    Get or set the use back-lobe gain as main-lobe attenuation flag.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelGaussian.efficiency
    :type: float

    Get or set the efficiency.


