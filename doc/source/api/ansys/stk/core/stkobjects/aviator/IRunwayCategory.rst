IRunwayCategory
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.IRunwayCategory

   object
   
   Interface used to access runways in the Aviator catalog.

.. py:currentmodule:: IRunwayCategory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRunwayCategory.user_runways`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRunwayCategory.arinc424_runways`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IRunwayCategory.dafif_runways`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRunwayCategory


Property detail
---------------

.. py:property:: user_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.user_runways
    :type: IUserRunwaySource

    Get the user runways.

.. py:property:: arinc424_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.arinc424_runways
    :type: IARINC424Source

    Get the ARINC-424 runways.

.. py:property:: dafif_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.dafif_runways
    :type: IDAFIFSource

    Get the DAFIF runways.


