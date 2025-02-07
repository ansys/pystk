Clouds
======

.. py:class:: ansys.stk.core.graphics.Clouds

   Load, show and hide clouds in the scene.

.. py:currentmodule:: Clouds

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Clouds.show`
              - Get or set whether clouds are rendered.
            * - :py:attr:`~ansys.stk.core.graphics.Clouds.clouds_uri`
              - The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.
            * - :py:attr:`~ansys.stk.core.graphics.Clouds.roundness`
              - The roundness of the clouds.
            * - :py:attr:`~ansys.stk.core.graphics.Clouds.altitude`
              - The altitude of the clouds.
            * - :py:attr:`~ansys.stk.core.graphics.Clouds.is_valid`
              - Return whether or not the clouds file is valid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Clouds


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.graphics.Clouds.show
    :type: bool

    Get or set whether clouds are rendered.

.. py:property:: clouds_uri
    :canonical: ansys.stk.core.graphics.Clouds.clouds_uri
    :type: str

    The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.

.. py:property:: roundness
    :canonical: ansys.stk.core.graphics.Clouds.roundness
    :type: float

    The roundness of the clouds.

.. py:property:: altitude
    :canonical: ansys.stk.core.graphics.Clouds.altitude
    :type: float

    The altitude of the clouds.

.. py:property:: is_valid
    :canonical: ansys.stk.core.graphics.Clouds.is_valid
    :type: bool

    Return whether or not the clouds file is valid.


