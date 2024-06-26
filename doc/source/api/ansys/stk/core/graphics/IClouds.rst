IClouds
=======

.. py:class:: ansys.stk.core.graphics.IClouds

   object
   
   Load, show and hide clouds in the scene.

.. py:currentmodule:: IClouds

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IClouds.show`
              - Gets or sets whether clouds are rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IClouds.clouds_uri`
              - The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.
            * - :py:attr:`~ansys.stk.core.graphics.IClouds.roundness`
              - The roundness of the clouds.
            * - :py:attr:`~ansys.stk.core.graphics.IClouds.altitude`
              - The altitude of the clouds.
            * - :py:attr:`~ansys.stk.core.graphics.IClouds.is_valid`
              - Returns whether or not the clouds file is valid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IClouds


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.graphics.IClouds.show
    :type: bool

    Gets or sets whether clouds are rendered.

.. py:property:: clouds_uri
    :canonical: ansys.stk.core.graphics.IClouds.clouds_uri
    :type: str

    The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.

.. py:property:: roundness
    :canonical: ansys.stk.core.graphics.IClouds.roundness
    :type: float

    The roundness of the clouds.

.. py:property:: altitude
    :canonical: ansys.stk.core.graphics.IClouds.altitude
    :type: float

    The altitude of the clouds.

.. py:property:: is_valid
    :canonical: ansys.stk.core.graphics.IClouds.is_valid
    :type: bool

    Returns whether or not the clouds file is valid.


