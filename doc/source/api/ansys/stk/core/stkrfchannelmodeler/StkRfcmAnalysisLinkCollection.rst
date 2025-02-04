StkRfcmAnalysisLinkCollection
=============================

.. py:class:: ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection

   A collection of links between transceivers.

.. py:currentmodule:: StkRfcmAnalysisLinkCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmAnalysisLinkCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IStkRfcmAnalysisLink
    :canonical: ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStkRfcmAnalysisLink`


