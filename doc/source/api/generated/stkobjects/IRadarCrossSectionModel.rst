IRadarCrossSectionModel
=======================

.. py:class:: IRadarCrossSectionModel

   object
   
   Provide access to the properties and methods defining a radar cross section model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~frequency_bands`


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
    :type: "IAgRadarCrossSectionFrequencyBandCollection"

    Gets the RCS frequency band collection.


