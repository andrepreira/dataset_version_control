# coding=utf-8
import collections
import re
from .regex import handle

class EventSearcher(object):

    def __init__(self, dataset_name):
        self.regex_list = handle.regex_from_file(dataset_name)
        self.events = collections.OrderedDict(self.regex_list)

        self.events_regex = {}

        for event in self.events.keys():
            self.events_regex[event] = []

            for regex in self.events[event]:
                regex = regex.replace(' ', r'\s*')
                self.events_regex[event].append(re.compile(regex, re.DOTALL | re.MULTILINE | re.IGNORECASE))

    def search(self, snippet):
        for event in self.events.keys():
            for keyword in self.events[event]:
                if keyword in snippet:
                    return event

            for regex in self.events_regex[event]:
                match = regex.search(snippet)
                if match is not None:
                    return event

        return None