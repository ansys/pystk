IVTOLPointCategory
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IVTOLPointCategory

   object
   
   Interface used to access the VTOL Points in the Aviator catalog.

.. py:currentmodule:: IVTOLPointCategory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.user_vtol_points`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.arinc424_helipads`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.dafif_helipads`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IVTOLPointCategory


Property detail
---------------

.. py:property:: user_vtol_points
    :canonical: ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.user_vtol_points
    :type: IUserVTOLPointSource

    Get the User VTOL Points.

.. py:property:: arinc424_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.arinc424_helipads
    :type: IARINC424Source

    Get the ARINC-424 helipads.

.. py:property:: dafif_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IVTOLPointCategory.dafif_helipads
    :type: IDAFIFSource

    Get the DAFIF helipads.


