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

    def __init__(self, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False):
        self.cached_name = False

        # FIXME use_handlers?
        super(HandlerBlock, self).__init__(
            play=play,
            parent_block=parent_block,
            role=role,
            task_include=task_include,
            use_handlers=use_handlers,
            implicit=implicit
        )

    def __repr__(self):
        return "HANDLERBLOCK(uuid=%s)(id=%s)(parent=%s)" % (self._uuid, id(self), self._parent)

    @staticmethod
    def load(data, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
        implicit = not Block.is_block(data)
        b = HandlerBlock(play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers, implicit=implicit)
        return b.load_data(data, variable_manager=variable_manager, loader=loader)

    def serialize(self):
        result = super(HandlerBlock, self).serialize()
        result['is_handler'] = True
        return result
