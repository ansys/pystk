CoverageAssetListElement
========================

.. py:class:: ansys.stk.core.stkobjects.CoverageAssetListElement

   Coverage asset.

.. py:currentmodule:: CoverageAssetListElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.contains_sub_assets`
              - Return whether or not this element has sub assets.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.asset_status`
              - Get or set the current status of the coverage asset (active or not).
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.grouping`
              - Opt whether to consider the members of a constellation as a group or as separate entities.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.object_name`
              - Name of the object assigned as a coverage asset.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.sub_asset_list`
              - Return the sub assets for this asset.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.required`
              - Flag sets whether Asset is required for all valid access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListElement.use_constellation_constraints`
              - Flag determines whether constellation constraints are considered.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageAssetListElement


Property detail
---------------

.. py:property:: asset_status
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.asset_status
    :type: CoverageAssetStatus

    Get or set the current status of the coverage asset (active or not).

.. py:property:: grouping
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.grouping
    :type: CoverageAssetGrouping

    Opt whether to consider the members of a constellation as a group or as separate entities.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.object_name
    :type: str

    Name of the object assigned as a coverage asset.

.. py:property:: sub_asset_list
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.sub_asset_list
    :type: CoverageAssetListCollection

    Return the sub assets for this asset.

.. py:property:: required
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.required
    :type: bool

    Flag sets whether Asset is required for all valid access intervals.

.. py:property:: use_constellation_constraints
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.use_constellation_constraints
    :type: bool

    Flag determines whether constellation constraints are considered.


Method detail
-------------






.. py:method:: contains_sub_assets(self) -> bool
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListElement.contains_sub_assets

    Return whether or not this element has sub assets.

    :Returns:

        :obj:`~bool`






