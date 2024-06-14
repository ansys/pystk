ICoverageAssetListElement
=========================

.. py:class:: ICoverageAssetListElement

   object
   
   Coverage asset.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~contains_sub_assets`
              - Return whether or not this element has sub assets.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~asset_status`
            * - :py:meth:`~grouping`
            * - :py:meth:`~object_name`
            * - :py:meth:`~sub_asset_list`
            * - :py:meth:`~required`
            * - :py:meth:`~use_const_constraints`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageAssetListElement


Property detail
---------------

.. py:property:: asset_status
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.asset_status
    :type: "COVERAGE_ASSET_STATUS"

    Gets or sets the current status of the coverage asset (active or not).

.. py:property:: grouping
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.grouping
    :type: "COVERAGE_ASSET_GROUPING"

    Opt whether to consider the members of a constellation as a group or as separate entities.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.object_name
    :type: str

    Name of the object assigned as a coverage asset.

.. py:property:: sub_asset_list
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.sub_asset_list
    :type: "IAgCvAssetListCollection"

    Returns the sub assets for this asset.

.. py:property:: required
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.required
    :type: bool

    Flag sets whether Asset is required for all valid access intervals.

.. py:property:: use_const_constraints
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListElement.use_const_constraints
    :type: bool

    Flag determines whether constellation constraints are considered.


Method detail
-------------






.. py:method:: contains_sub_assets(self) -> bool

    Return whether or not this element has sub assets.

    :Returns:

        :obj:`~bool`






