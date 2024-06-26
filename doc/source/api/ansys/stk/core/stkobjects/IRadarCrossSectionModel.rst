IRadarCrossSectionModel
=======================

.. py:class:: ansys.stk.core.stkobjects.IRadarCrossSectionModel

   object
   
   Provide access to the properties and methods defining a radar cross section model.

.. py:currentmodule:: IRadarCrossSectionModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionModel.name`
              - Gets the radar cross section model name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionModel.frequency_bands`
              - Gets the RCS frequency band collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionModel.name
    :type: str

    Gets the radar cross section model name.

.. py:property:: frequency_bands
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionModel.frequency_bands
    :type: IRadarCrossSectionFrequencyBandCollection

    Gets the RCS frequency band collection.


