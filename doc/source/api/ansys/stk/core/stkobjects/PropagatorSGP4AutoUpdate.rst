PropagatorSGP4AutoUpdate
========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate

   SGP4 AutoUpdate.

.. py:currentmodule:: PropagatorSGP4AutoUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.selected_source`
              - Get or set the source type for element updates.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.properties`
              - Get the Automatic Update selection and method.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.file_source`
              - A file to be used as the element source, containing GP data (either TLEs or CCSDS OMM content).
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.online_source`
              - AGI server to be used as the element source.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4AutoUpdate


Property detail
---------------

.. py:property:: selected_source
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.selected_source
    :type: VehicleSGP4AutomaticUpdateSourceType

    Get or set the source type for element updates.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.properties
    :type: PropagatorSGP4AutoUpdateProperties

    Get the Automatic Update selection and method.

.. py:property:: file_source
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.file_source
    :type: PropagatorSGP4AutoUpdateFileSource

    A file to be used as the element source, containing GP data (either TLEs or CCSDS OMM content).

.. py:property:: online_source
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate.online_source
    :type: PropagatorSGP4AutoUpdateOnlineSource

    AGI server to be used as the element source.


