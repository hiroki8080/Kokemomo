#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .km_session_manager import get_value_to_session

__author__ = 'hiroki-m'


class KMData():

    def __init__(self, controller):
        self.controller = controller

    def get_request(self):
        return self.controller.plugin.get_request()

    def get_response(self):
        return self.controller.plugin.get_response()

    def get_request_parameter(self, name, default=None):
        return self.controller.plugin.get_request_parameter(name, default)

    def get_user_id(self):
        request = self.controller.plugin.get_request()
        return get_value_to_session(request, 'user_id')
