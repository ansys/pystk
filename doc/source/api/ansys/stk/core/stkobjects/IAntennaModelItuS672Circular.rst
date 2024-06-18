IAntennaModelItuS672Circular
============================

.. py:class:: IAntennaModelItuS672Circular

   object
   
   Provide access to the properties and methods defining an ITU-R S672-4 circular antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~efficiency`
            * - :py:meth:`~diameter`
            * - :py:meth:`~use_mainlobe_model`
            * - :py:meth:`~override_half_beamwidth`
            * - :py:meth:`~half_beamwidth`
            * - :py:meth:`~nearin_sidelobe_level`
            * - :py:meth:`~farout_sidelobe_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelItuS672Circular


Property detail
---------------

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.mainlobe_gain
    :type: float

    Gets or sets the main-lobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: use_mainlobe_model
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.use_mainlobe_model
    :type: bool

    Gets or sets the option for enabling the mainlobe model.

.. py:property:: override_half_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.override_half_beamwidth
    :type: bool

    Gets or sets the option for overriding the half beamwidth.

.. py:property:: half_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.half_beamwidth
    :type: typing.Any

    Gets or sets the half beamwidth.

.. py:property:: nearin_sidelobe_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.nearin_sidelobe_level
    :type: float

    Gets or sets the near in sidelobe level.

.. py:property:: farout_sidelobe_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelItuS672Circular.farout_sidelobe_level
    :type: float

    Gets or sets the far out sidelobe level.


