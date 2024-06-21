IDataProviderResultSubSection
=============================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultSubSection

   object
   
   Represents a sub-section data element.

.. py:currentmodule:: IDataProviderResultSubSection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultSubSection.title`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultSubSection.intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultSubSection


Property detail
---------------

.. py:property:: title
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultSubSection.title
    :type: str

    Returns a title of the sub-section.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultSubSection.intervals
    :type: IDataProviderResultIntervalCollection

    Returns a collection of intervals within the sub-section.


