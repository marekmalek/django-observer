#!/usr/bin/env python
"""
A set of callback types


AUTHOR:
    Marek Malek (marek.malek@ymail.com)
    
Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__AUTHOR__ = "Marek Malek (marek.malek@ymail.com)"

class ObserverCallback(object):
    def __init__(self, callback):
        self.callback = callback
        
class CallFunction(ObserverCallback):
    pass

class CallMethod(ObserverCallback):
    pass