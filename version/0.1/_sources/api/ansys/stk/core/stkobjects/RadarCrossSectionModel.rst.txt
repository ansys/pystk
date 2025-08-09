RadarCrossSectionModel
======================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a radar cross section model.

.. py:currentmodule:: RadarCrossSectionModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionModel.name`
              - Get the radar cross section model name.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionModel.frequency_bands`
              - Get the RCS frequency band collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionModel.name
    :type: str

    Get the radar cross section model name.

.. py:property:: frequency_bands
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionModel.frequency_bands
    :type: RadarCrossSectionFrequencyBandCollection

    Get the RCS frequency band collection.


