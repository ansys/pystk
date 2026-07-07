AntennaModelHFSSDesign
======================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelHFSSDesign

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an HFSS design antenna model.

.. py:currentmodule:: AntennaModelHFSSDesign

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHFSSDesign.generate`
              - Generate the HFSS design antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHFSSDesign.set_design_type`
              - Set the HFSS design type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHFSSDesign.availability`
              - Get the availability of the HFSS design antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHFSSDesign.design`
              - Get the HFSS design.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelHFSSDesign.status`
              - Get the status of the HFSS design antenna.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelHFSSDesign


Property detail
---------------

.. py:property:: availability
    :canonical: ansys.stk.core.stkobjects.AntennaModelHFSSDesign.availability
    :type: str

    Get the availability of the HFSS design antenna.

.. py:property:: design
    :canonical: ansys.stk.core.stkobjects.AntennaModelHFSSDesign.design
    :type: IAntennaHFSSDesign

    Get the HFSS design.

.. py:property:: status
    :canonical: ansys.stk.core.stkobjects.AntennaModelHFSSDesign.status
    :type: AntennaHFSSDesignStatus

    Get the status of the HFSS design antenna.


Method detail
-------------



.. py:method:: generate(self) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaModelHFSSDesign.generate

    Generate the HFSS design antenna.

    :Returns:

        :obj:`~None`

.. py:method:: set_design_type(self, type: AntennaHFSSDesignType) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaModelHFSSDesign.set_design_type

    Set the HFSS design type.

    :Parameters:

        **type** : :obj:`~AntennaHFSSDesignType`


    :Returns:

        :obj:`~None`


