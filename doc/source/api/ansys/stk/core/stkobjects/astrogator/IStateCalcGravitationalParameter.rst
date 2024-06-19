IStateCalcGravitationalParameter
================================

.. py:class:: IStateCalcGravitationalParameter

   object
   
   Properties for a Gravitational Parameter calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~grav_source`
            * - :py:meth:`~gravity_filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcGravitationalParameter


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravitationalParameter.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: grav_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravitationalParameter.grav_source
    :type: GRAVITATIONAL_PARAMETER_SOURCE

    Gets or sets the source for the gravitational parameter.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcGravitationalParameter.gravity_filename
    :type: str

    Source for the gravitational parameter if GravSource is set to Gravity File.


