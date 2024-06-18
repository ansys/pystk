ICentralBodyGraphicsIndexer
===========================

.. py:class:: ICentralBodyGraphicsIndexer

   object
   
   An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the central body graphics for the specified central body.
            * - :py:meth:`~get_by_name`
              - Return the central body graphics for the central body with the given name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~earth`
            * - :py:meth:`~moon`
            * - :py:meth:`~sun`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICentralBodyGraphicsIndexer


Property detail
---------------

.. py:property:: earth
    :canonical: ansys.stk.core.graphics.ICentralBodyGraphicsIndexer.earth
    :type: "IAgStkGraphicsCentralBodyGraphics"

    Gets the central body graphics for the planet Earth. This is equivalent to passing a central body equal to an instance of earth central body to the indexer.

.. py:property:: moon
    :canonical: ansys.stk.core.graphics.ICentralBodyGraphicsIndexer.moon
    :type: "IAgStkGraphicsCentralBodyGraphics"

    Gets the central body graphics for the Moon.

.. py:property:: sun
    :canonical: ansys.stk.core.graphics.ICentralBodyGraphicsIndexer.sun
    :type: "IAgStkGraphicsCentralBodyGraphics"

    Gets the central body graphics for the Sun.


Method detail
-------------




.. py:method:: item(self, centralBody:str) -> "ICentralBodyGraphics"

    Get the central body graphics for the specified central body.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~"ICentralBodyGraphics"`

.. py:method:: get_by_name(self, name:str) -> "ICentralBodyGraphics"

    Return the central body graphics for the central body with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"ICentralBodyGraphics"`

