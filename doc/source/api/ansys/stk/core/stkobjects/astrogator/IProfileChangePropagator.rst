IProfileChangePropagator
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator

   IProfile
   
   Properties for a Change Propagator profile.

.. py:currentmodule:: IProfileChangePropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.set_segment`
              - Set the targeted segment.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.segment_name`
              - Gets or sets the name of the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.propagator_name`
              - Gets or sets the new propagator's name.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangePropagator


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.segment_name
    :type: str

    Gets or sets the name of the profile.

.. py:property:: propagator_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.propagator_name
    :type: str

    Gets or sets the new propagator's name.


Method detail
-------------



.. py:method:: set_segment(self, pVAMCSSegment: IMissionControlSequenceSegment) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator.set_segment

    Set the targeted segment.

    :Parameters:

    **pVAMCSSegment** : :obj:`~IMissionControlSequenceSegment`

    :Returns:

        :obj:`~None`



