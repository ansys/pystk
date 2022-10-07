# Copyright 2020-2020, Analytical Graphics, Inc. 
'''
This module contains specific exceptions that may be raised from the STK API.
'''


class STKInitializationError(RuntimeError):
    '''
    Raised in STKDesktop and STKEngine when unable to initialize or attach to STK.
    '''
    
class STKInvalidCastError(RuntimeError):
    '''
    Raised when attempting to cast an object to an unsupported interface or class type.
    '''
    
class STKRuntimeError(RuntimeError):
    '''
    Raised when an STK method call fails.
    '''
    
class STKAttributeError(AttributeError):
    '''
    Raised when attempting to set an unrecognized attribute within the STK API.
    '''
    
class STKEventsAPIError(SyntaxError):
    '''
    Raised when attempting to assign to an STK Event rather than using operator += or -=.
    '''
    
class STKPluginMethodNotImplementedError(SyntaxError):
    '''
    Raised when a plugin method is called by STK that was not implemented by the user.
    '''
    
class STKInvalidTimerError(RuntimeError):
    '''
    Raised when attempting to use an engine timer that cannot be implemented.
    '''
    
class STKColorError(RuntimeError):
    '''
    Raised when a problem is encountered with color classes.
    '''