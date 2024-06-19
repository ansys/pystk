IRunwayCategory
===============

.. py:class:: IRunwayCategory

   object
   
   Interface used to access runways in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~user_runways`
            * - :py:meth:`~arinc424_runways`
            * - :py:meth:`~dafif_runways`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRunwayCategory


Property detail
---------------

.. py:property:: user_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.user_runways
    :type: IAgAvtrUserRunwaySource

    Get the user runways.

.. py:property:: arinc424_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.arinc424_runways
    :type: IAgAvtrARINC424Source

    Get the ARINC-424 runways.

.. py:property:: dafif_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IRunwayCategory.dafif_runways
    :type: IAgAvtrDAFIFSource

    Get the DAFIF runways.


