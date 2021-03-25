# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.playbook.attribute import FieldAttribute
from ansible.playbook.block import Block
from ansible.module_utils.six import string_types


class HandlerBlock(Block):

    _listen = FieldAttribute(isa='list', default=list, listof=string_types, static=True)

    def __init__(self, play=None, parent_block=None, role=None, task_include=None, implicit=False):
        self.cached_name = False

        super(HandlerBlock, self).__init__(
            play=play,
            parent_block=parent_block,
            role=role,
            task_include=task_include,
            implicit=False,
        )

        self._use_handlers = True

    def __repr__(self):
        return "HANDLERBLOCK(uuid=%s)(id=%s)(parent=%s)" % (self._uuid, id(self), self._parent)

    def get_name(self, include_role_fqcn=True):
        '''Return the name of the block'''
        if self._role:
            role_name = self._role.get_name(include_role_fqcn=include_role_fqcn)

        if self._role and self.name:
            return "%s : %s" % (role_name, self.name)

        return self.name

    @staticmethod
    def load(data, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
        b = HandlerBlock(play=play, parent_block=parent_block, role=role, task_include=task_include, implicit=False)
        return b.load_data(data, variable_manager=variable_manager, loader=loader)
