# coding: utf-8
# Copyright: (c) 2019, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import ast

from ansible.errors import AnsibleAssertionError
from ansible.module_utils.common._collections_compat import Iterable
from ansible.module_utils.six import string_types


def isidentifier(ident):
    """
    Determines, if string is valid Python identifier using the ast module.
    Originally posted at: http://stackoverflow.com/a/29586366
    """

    if not isinstance(ident, string_types):
        return False

    try:
        root = ast.parse(ident)
    except SyntaxError:
        return False

    if not isinstance(root, ast.Module):
        return False

    if len(root.body) != 1:
        return False

    if not isinstance(root.body[0], ast.Expr):
        return False

    if not isinstance(root.body[0].value, ast.Name):
        return False

    if root.body[0].value.id != ident:
        return False

    return True


def validate_variable_names(names):
    """
    This checks that all variable names are valid or raises an error.

    :arg data: iterable of names
    :raises TypeError: if one of the variable names is not valid
    :raises AnsibleError: if one of the variable names is a reserved name and ANSIBLE_RESERVED_VAR_NAMES=error
    """

    # avoid circular imports
    from ansible.vars.reserved import handle_reserved_vars

    if not isinstance(names, Iterable):
        raise AnsibleAssertionError("'names' must be of type <Iterable>, was: %s" % type(names))

    for name in names:
        if not isidentifier(name):
            raise TypeError(
                "The variable name '%s' is not valid. Variables must start with a letter or underscore "
                "character, and contain only letters, numbers and underscores." % name
            )

    handle_reserved_vars(names)
