AnalysisLinkCollection
======================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection

   A collection of links between transceivers.

.. py:currentmodule:: AnalysisLinkCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import AnalysisLinkCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAnalysisLink
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IAnalysisLink`


